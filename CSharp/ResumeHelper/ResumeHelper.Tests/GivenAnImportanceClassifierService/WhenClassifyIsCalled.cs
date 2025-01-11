using FluentAssertions;
using ResumeHelper.Domain;
using ResumeHelper.Services;

namespace ResumeHelper.Tests.GivenAnImportanceClassifierService;

[TestFixture]
public class WhenClassifyIsCalled : TestBase
{
    [TestCase("a", KeywordImportance.Low)]
    [TestCase("A", KeywordImportance.Low)]
    [TestCase("Data", KeywordImportance.Medium)]
    public void ThenReturnsExpectedImportance(
        string word, KeywordImportance expectedImportance)
    {
        // Arrange
        var SUT = new ImportanceClassifierService(LOW_IMPORTANCE_WORDS_PATH);

        // Act
        var result = SUT.Classify(word);

        // Assert
        result.Should().Be(expectedImportance);
    }
}