namespace ResumeHelper.Domain;

public class KeyWord(
    string word,
    KeywordImportance importance = KeywordImportance.Medium,
    bool isMatch = false)
{
    public readonly string Word = word;
    public KeywordImportance Importance { get; internal set; } = importance;
    public bool IsMatch { get; internal set; } = isMatch;
    
    public ConsoleColor ForegroundColor => IsMatch ? ConsoleColor.White : ImportanceColor;
    public ConsoleColor BackgroundColor => IsMatch ? ImportanceColor : ConsoleColor.Black;

    private ConsoleColor ImportanceColor => Importance switch
    {
        KeywordImportance.High => ConsoleColor.Red,
        KeywordImportance.Medium => ConsoleColor.Green,
        KeywordImportance.Low => ConsoleColor.DarkGray,
        _ => ConsoleColor.DarkGray
    };

    public override string ToString()
    {
        return $"{Word}";
    }
}