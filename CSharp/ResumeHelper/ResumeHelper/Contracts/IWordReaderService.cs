using ResumeHelper.Domain;

namespace ResumeHelper.Contracts;

public interface IWordReaderService : IDisposable
{
    IEnumerable<KeyWord> ReadWords(string filePath);
}