using FluentAssertions;
using ResumeHelper.Contracts;
using ResumeHelper.Domain;
using ResumeHelper.Services;
using NSubstitute;

namespace ResumeHelper.Tests.GivenAResumeMatchingService;

[TestFixture]
public class WhenMatchIsCalled : TestBase
{
    [Test]
    public void ThenReturnsMatchResult()
    {
        // Arrange
        var SUT = CreateSUT();

        // Act
        var result = SUT.Match(TEST_RESUME_FILE_PATH, TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        result.Should().BeOfType<MatchResult>();
    }

    [Test]
    public void ThenKeyWordsAreReturnedFromJobDescription()
    {
        // Arrange
        var dummyWordReaderService = Substitute.For<IWordReaderService>();
        dummyWordReaderService.ReadWords(Arg.Any<string>())
            .Returns([new KeyWord("Job")]);
        var SUT = CreateSUT(dummyWordReaderService);

        // Act
        var result = SUT.Match(TEST_RESUME_FILE_PATH, TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        var keyWord = result.KeyWords.First();
        keyWord.Word.Should().Be("Job");
    }

    [TestCase("a", KeywordImportance.Low)]
    [TestCase("Data", KeywordImportance.Medium)]
    public void ThenLowAndMediumImportanceWordsAreReturnedAsExpected(
        string word, KeywordImportance expectedImportance)
    {
        // Arrange
        var dummyWordReaderService = Substitute.For<IWordReaderService>();
        dummyWordReaderService.ReadWords(Arg.Any<string>())
            .Returns([new KeyWord(word)]);
        var classifierService = new ImportanceClassifierService(LOW_IMPORTANCE_WORDS_PATH);
        var SUT = CreateSUT(dummyWordReaderService, classifierService);

        // Act
        var result = SUT.Match(TEST_RESUME_FILE_PATH, TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        var keyWord = result.KeyWords.First();
        keyWord.Importance.Should().Be(expectedImportance);
    }

    [Test]
    public void ThenLowImportanceWordsAreReturnedAsLowImportance()
    {
        // Arrange
        var wordReaderService = new WordReaderService();
        var classifierService = new ImportanceClassifierService(LOW_IMPORTANCE_WORDS_PATH);
        var SUT = CreateSUT(wordReaderService, classifierService);

        // Act
        var result = SUT.Match(TEST_RESUME_FILE_PATH, TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        result.KeyWords.Should().BeEquivalentTo(new List<KeyWord>
        {
            new("Job", KeywordImportance.Medium),
            new("Description", KeywordImportance.Medium),
            new("We", KeywordImportance.Low),
            new("are", KeywordImportance.Low),
            new("looking", KeywordImportance.Medium),
            new("for", KeywordImportance.Low),
            new("a", KeywordImportance.Low),
            new("Data", KeywordImportance.High, true),
            new("Architect", KeywordImportance.High, true)
        });
    }

    private static ResumeMatchingService CreateSUT(
        IWordReaderService wordReaderService = null,
        IImportanceClassifierService importanceClassifierService = null)
    {
        return new ResumeMatchingService(
            wordReaderService ?? Substitute.For<IWordReaderService>(),
            importanceClassifierService ?? Substitute.For<IImportanceClassifierService>()
        );
    }
}