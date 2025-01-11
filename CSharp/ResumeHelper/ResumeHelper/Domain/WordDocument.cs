namespace ResumeHelper.Domain;

public class WordDocument
{
    public string FilePath { get; }

    public WordDocument(string filePath)
    {
        FilePath = filePath;
    }
}
