using ResumeHelper.Contracts;
using ResumeHelper.Domain;

namespace ResumeHelper.Services;

public class ImportanceClassifierService(string lowImportanceWordsPath) : IImportanceClassifierService
{
    private readonly HashSet<string> _lowImportanceWords = File.ReadAllLines(lowImportanceWordsPath)
        .Select(w => w.ToLower().Trim())
        .Where(w => !string.IsNullOrWhiteSpace(w))
        .ToHashSet();

    public KeywordImportance Classify(string word)
    {
        return _lowImportanceWords.Contains(word, StringComparer.OrdinalIgnoreCase) 
            ? KeywordImportance.Low 
            : KeywordImportance.Medium;
    }
}