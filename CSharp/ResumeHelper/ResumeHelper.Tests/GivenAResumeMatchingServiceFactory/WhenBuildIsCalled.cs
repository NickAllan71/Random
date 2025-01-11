using FluentAssertions;
using ResumeHelper.Factories;
using ResumeHelper.Services;

namespace ResumeHelper.Tests.GivenAResumeMatchingServiceFactory;

[TestFixture]
public class WhenBuildIsCalled
{
    [Test]
    public void ThenReturnsResumeMatchingService()
    {
        // Act
        var result = ResumeMatchingServiceFactory.Build();
        
        // Assert
        result.Should().BeOfType<ResumeMatchingService>();
    }
}