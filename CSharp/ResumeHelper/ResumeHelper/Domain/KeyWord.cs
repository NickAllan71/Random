namespace ResumeHelper.Domain;

public class KeyWord(
    string word,
    KeywordImportance importance = KeywordImportance.Medium)
{
    public readonly string Word = word;
    public KeywordImportance Importance { get; set; } = importance;
}