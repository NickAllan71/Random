using FluentAssertions;
using ResumeHelper.Services;

namespace ResumeHelper.Tests.GivenAFileHandlerService;

[TestFixture]
public class WhenDiscoverIsCalled : TestBase
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void ThenReturnsFilePathAsString()
    {
        // Arrange
        var SUT = new FileHandlerService();

        // Act
        var result = SUT.Discover(TEST_ROOT_PATH).First();

        // Assert
        result.Should().BeOfType<string>();
    }

    [TestCase("*resume*.docx", ".docx")]
    [TestCase("*job*desc*.docx", ".docx")]
    [TestCase("*.txt", "")]
    public void WithFileSpecReturnsMatchingFiles(string fileSpec, string expectedExtension)
    {
        // Arrange
        var SUT = new FileHandlerService();

        // Act
        var result = SUT.Discover(TEST_ROOT_PATH, fileSpec).FirstOrDefault(string.Empty);

        // Assert
        result.Should().EndWith(expectedExtension);
    }

    [Test]
    public void WithRecursiveChecksSubdirectories()
    {
        // Arrange
        var SUT = new FileHandlerService();

        // Act
        var result = SUT.Discover(
            TEST_ROOT_PATH, "RecursiveResumeTestFile.docx", true).Single();

        // Assert
        result.Should().BeOfType<string>();
    }
}