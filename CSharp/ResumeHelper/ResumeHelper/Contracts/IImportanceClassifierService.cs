using ResumeHelper.Domain;

namespace ResumeHelper.Contracts;

public interface IImportanceClassifierService
{
    KeywordImportance Classify(string word);
}