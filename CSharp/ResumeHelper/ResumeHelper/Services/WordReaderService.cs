using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using ResumeHelper.Contracts;
using ResumeHelper.Domain;
using System.Text.RegularExpressions;

namespace ResumeHelper.Services;

public class WordReaderService : IWordReaderService, IDisposable
{
    private List<string> _tempFilePaths = new();

    public IEnumerable<KeyWord> ReadWords(string filePath)
    {
        foreach (var paragraph in GetParagraphs(filePath))
            foreach (var word in ProcessParagraph(paragraph))
                yield return word;
    }

    private IEnumerable<Paragraph> GetParagraphs(string filePath)
    {
        using var docx = OpenDocx(filePath);
        var body = docx.MainDocumentPart?.Document?.Body;
        if (body == null)
            yield break;
        
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

    private WordprocessingDocument OpenDocx(string filePath)
    {
        try
        {
            return WordprocessingDocument.Open(filePath, false);
        }
        catch (IOException)
        {
            var tempFilePath = CopyToTempFilePath(filePath);
            return WordprocessingDocument.Open(tempFilePath, false);
        }
        catch (Exception ex)
        {
            throw new Exception(
                $"Error opening file: {filePath}", ex);
        }
    }

    private string CopyToTempFilePath(string filePath)
    {
        var tempFilePath = Path.GetTempFileName();
        File.Copy(filePath, tempFilePath, true);
        _tempFilePaths.Add(tempFilePath);

        return tempFilePath;
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
                    Importance = isHighlighted ? KeywordImportance.High : KeywordImportance.Medium
                };
        }
    }

    public void Dispose()
    {
        foreach (var tempFilePath in _tempFilePaths)
            File.Delete(tempFilePath);
    }
}