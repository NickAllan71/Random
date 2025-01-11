using ResumeHelper.Services;

namespace ResumeHelper.Factories;

public class ResumeMatchingServiceFactory()
{
    private static readonly string _lowImportanceWordsPath = Path.Combine(
        AppContext.BaseDirectory, "..", "..", "..", "..", 
        "ResumeHelper", "Config",
        "LowImportanceWords.txt");

    public static ResumeMatchingService Build()
    {
        return new ResumeMatchingService(
            new WordReaderService(),
            new ImportanceClassifierService(_lowImportanceWordsPath));
    }
}