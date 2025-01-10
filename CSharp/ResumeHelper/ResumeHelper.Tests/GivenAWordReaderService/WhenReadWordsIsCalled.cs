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
        var filePath = Path.Combine(
            TEST_ROOT_PATH, @"JobDescriptionTestFile.docx");

        // Act
        using var SUT = new WordReaderService(filePath);
        var results = SUT.ReadWords();

        // Assert
        results.Select(w => new KeyWord(w.Word))
            .Should().BeEquivalentTo(expected);
    }

    private static IEnumerable<KeyWord> GetExpected(string sentence)
    {
        return sentence.Split(" ").Select(w => new KeyWord(w));
    }

    [Test]
    public void ThenHighlightedKeyWordsAreReturned()
    {
        // Arrange
        var expected = GetExpected("Data Architect");
        var filePath = Path.Combine(
            TEST_ROOT_PATH, @"JobDescriptionTestFile.docx");

        // Act
        using var SUT = new WordReaderService(filePath);
        var result = SUT.ReadWords();

        // Assert
        result.Select(w => w)
            .Where(w => w.Importance == EnumKeywordImportance.High)
            .Count().Should().Be(2);
    }
}
