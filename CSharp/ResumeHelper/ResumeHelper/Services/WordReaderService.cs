using DocumentFormat.OpenXml.Office2013.PowerPoint.Roaming;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using ResumeHelper.Domain;
using System.Text.RegularExpressions;

namespace ResumeHelper.Services;

public class WordReaderService : IDisposable
{
    private readonly string _filePath;
    private string _tempFilePath = string.Empty;

    public WordReaderService(string filePath)
    {
        _filePath = filePath;
    }

    public IEnumerable<KeyWord> ReadWords()
    {
        foreach (var paragraph in GetParagraphs())
            foreach (var word in ProcessParagraph(paragraph))
                yield return word;
    }

    private IEnumerable<Paragraph> GetParagraphs()
    {
        using var docx = GetDocx();
        var body = docx.MainDocumentPart?.Document?.Body;
        
        foreach (var element in body.ChildElements)
        {
            if (element is Paragraph paragraph)
            {
                yield return paragraph;
            }
            else if (element is Table table)
            {
                foreach (var row in table.Elements<TableRow>())
                    foreach (var cell in row.Elements<TableCell>())
                        foreach (var cellElement in cell.ChildElements)
                            if (cellElement is Paragraph cellParagraph)
                                yield return cellParagraph;
            }
        }
    }

    private static IEnumerable<string> GetWordsFromString(string text)
    {
        foreach (var word in Regex.Split(text, @"\W+"))
            if (!string.IsNullOrEmpty(word))
                yield return word;
    }

    private WordprocessingDocument GetDocx()
    {
        try
        {
            return WordprocessingDocument.Open(_filePath, false);
        }
        catch (IOException)
        {
            CopyToTempFilePath();
            return WordprocessingDocument.Open(_tempFilePath, false);
        }
        catch (Exception ex)
        {
            throw new Exception(
                $"Error opening file: {_filePath}", ex);
        }
    }

    private void CopyToTempFilePath()
    {
        _tempFilePath = Path.GetTempFileName();
        File.Copy(_filePath, _tempFilePath, true);
    }

    private IEnumerable<KeyWord> ProcessParagraph(Paragraph paragraph)
    {
        foreach (var run in paragraph.Elements<Run>())
        {
            var runProps = run.GetFirstChild<RunProperties>();
            var isHighlighted = runProps?.Highlight?.Val != null
                && runProps.Highlight.Val == HighlightColorValues.Yellow;
            
            foreach (var word in GetWordsFromString(run.InnerText))
                yield return new KeyWord(word)
                {
                    Importance = isHighlighted ? EnumKeywordImportance.High : EnumKeywordImportance.Medium
                };
        }
    }

    public void Dispose()
    {
        if (_tempFilePath != string.Empty)
            File.Delete(_tempFilePath);
    }
}