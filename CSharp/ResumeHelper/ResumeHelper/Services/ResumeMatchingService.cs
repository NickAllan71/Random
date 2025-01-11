using ResumeHelper.Contracts;
using ResumeHelper.Domain;

namespace ResumeHelper.Services
{
    public class ResumeMatchingService(IWordReaderService wordReaderService)
    {
        private readonly IWordReaderService _wordReaderService = wordReaderService;
        
        public MatchResult Match(string resumeFilePath, string jobDescriptionFilePath)
        {
            var matchResult = new MatchResult();
            foreach (var keyWord in _wordReaderService.ReadWords(resumeFilePath))
            {
                keyWord.Importance = KeywordImportance.Low;
                matchResult.AddKeyWord(keyWord);
            }
            return matchResult;
        }
    }
}