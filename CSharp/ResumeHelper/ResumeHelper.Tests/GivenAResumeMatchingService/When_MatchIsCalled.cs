using FluentAssertions;
using ResumeHelper.Contracts;
using ResumeHelper.Domain;
using ResumeHelper.Services;
using NSubstitute;

namespace ResumeHelper.Tests.GivenAResumeMatchingService;

[TestFixture]
public class When_MatchIsCalled : TestBase
{
    [Test]
    public void ThenReturnsMatchResult()
    {
        // Arrange
        var SUT = createSUT();

        // Act
        var result = SUT.Match(TEST_RESUME_FILE_PATH, TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        result.Should().BeOfType<MatchResult>();
    }

    [Test]
    public void ThenKeyWordsAreReturnedFromResume()
    {
        // Arrange
        var dummyWordReaderService = Substitute.For<IWordReaderService>();
        dummyWordReaderService.ReadWords(Arg.Any<string>())
            .Returns(new [] { new KeyWord("Nick") });
        var SUT = createSUT(dummyWordReaderService);

        // Act
        var result = SUT.Match(TEST_RESUME_FILE_PATH, TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        var keyWord = result.KeyWords.First();
        keyWord.Word.Should().Be("Nick");
    }

    [TestCase("a", KeywordImportance.Low)]
    //[TestCase("Data", KeywordImportance.High)]
    public void WithLowImporanceWords_ThenImportanceEqualsLow(
        string word, KeywordImportance expectedImportance)
    {
        // Arrange
        var dummyWordReaderService = Substitute.For<IWordReaderService>();
        dummyWordReaderService.ReadWords(Arg.Any<string>())
            .Returns(new [] { new KeyWord(word) });
        var SUT = createSUT(dummyWordReaderService);

        // Act
        var result = SUT.Match(TEST_RESUME_FILE_PATH, TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        var keyWord = result.KeyWords.First();
        keyWord.Importance.Should().Be(expectedImportance);
    }

    private static ResumeMatchingService createSUT(
        IWordReaderService wordReaderService = null)
    {
        return new ResumeMatchingService(
            wordReaderService ?? Substitute.For<IWordReaderService>()
        );
    }
}