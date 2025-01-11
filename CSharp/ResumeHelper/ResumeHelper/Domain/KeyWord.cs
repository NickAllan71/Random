namespace ResumeHelper.Domain;

public class KeyWord(
    string word,
    KeywordImportance importance = KeywordImportance.Medium,
    bool isMatch = false)
{
    public readonly string Word = word;
    public KeywordImportance Importance { get; internal set; } = importance;
    public bool IsMatch { get; internal set; } = isMatch;

    public override string ToString()
    {
        return $"{Word}";
    }
}