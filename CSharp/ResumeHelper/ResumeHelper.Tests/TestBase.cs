namespace ResumeHelper.Tests;

public abstract class TestBase
{
    private static readonly string SOLUTION_ROOT_PATH = Path.GetFullPath(
        Path.Combine(AppContext.BaseDirectory, "..", "..", "..", ".."));
    protected static readonly string TEST_ROOT_PATH = Path.Combine(
        SOLUTION_ROOT_PATH, "ResumeHelper.Tests", "TestFiles");
    protected static readonly string TEST_JOB_DESCRIPTION_FILE_PATH = GetTestDocxPath("JobDescriptionTestFile.docx");
    protected static readonly string TEST_RESUME_FILE_PATH = GetTestDocxPath("ResumeTestFile.docx");
    protected static string LOW_IMPORTANCE_WORDS_PATH => Path.Combine(
        SOLUTION_ROOT_PATH, "ResumeHelper", "Config", "LowImportanceWords.txt");

    private static string GetTestDocxPath(string wordFilePath) => Path.Combine(
        SOLUTION_ROOT_PATH, "ResumeHelper.Tests", "TestFiles", wordFilePath);
}