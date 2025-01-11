using ResumeHelper.Domain;

namespace ResumeHelper.Services;

public class ImportanceClassifierService
{
    private readonly HashSet<string> _lowImportanceWords;

    public ImportanceClassifierService(string lowImportanceWordsPath)
    {
        _lowImportanceWords = File.ReadAllLines(lowImportanceWordsPath)
            .Select(w => w.ToLower().Trim())
            .Where(w => !string.IsNullOrWhiteSpace(w))
            .ToHashSet();
    }

    public KeywordImportance Classify(string word)
    {
        return _lowImportanceWords.Contains(word.ToLower()) 
            ? KeywordImportance.Low 
            : KeywordImportance.Medium;
    }
}
