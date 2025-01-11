using FluentAssertions;
using NUnit.Framework.Internal;
using ResumeHelper.Domain;
using ResumeHelper.Services;

namespace ResumeHelper.Tests.GivenAWordReaderService;

[TestFixture]
public class WhenReadWordsIsCalled : TestBase
{
    [Test]
    public void ThenKeyWordsAreReturned()
    {
        // Arrange
        var expected = GetExpected(
            "Job Description We are looking for a Data Architect");
        using var SUT = new WordReaderService();

        // Act
        var results = SUT.ReadWords(TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        results.Select(w => new KeyWord(w.Word))
            .Should().BeEquivalentTo(expected);
    }

    [Test]
    public void ThenHighlightedKeyWordsAreReturned()
    {
        // Arrange
        using var SUT = new WordReaderService();

        // Act
        var result = SUT.ReadWords(TEST_JOB_DESCRIPTION_FILE_PATH);

        // Assert
        result.Select(w => w)
            .Where(w => w.Importance == KeywordImportance.High)
            .Count().Should().Be(2);
    }

    private static IEnumerable<KeyWord> GetExpected(string sentence)
    {
        return sentence.Split(" ").Select(w => new KeyWord(w));
    }
}