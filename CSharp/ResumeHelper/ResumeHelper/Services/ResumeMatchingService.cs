using ResumeHelper.Contracts;
using ResumeHelper.Domain;

namespace ResumeHelper.Services
{
    public class ResumeMatchingService(
        IWordReaderService wordReaderService,
        IImportanceClassifierService importanceClassifierService)
    {
        private readonly IWordReaderService _wordReaderService = wordReaderService;
        private readonly IImportanceClassifierService _importanceClassifierService = importanceClassifierService;
        
        public MatchResult Match(string resumeFilePath, string jobDescriptionFilePath)
        {
            var resumeKeyWords = GetResumeKeyWords(resumeFilePath);
            var matchResult = new MatchResult();

            foreach (var keyWord in _wordReaderService.ReadWords(jobDescriptionFilePath))
            {
                var importance = _importanceClassifierService.Classify(keyWord.Word);
                if (importance == KeywordImportance.Low)
                {
                    keyWord.Importance = importance;
                }
                else
                {
                    keyWord.IsMatch = resumeKeyWords.Any(
                        kw => kw.Word.Equals(keyWord.Word, StringComparison.OrdinalIgnoreCase));
                }
                matchResult.AddKeyWord(keyWord);
            }
            
            return matchResult;
        }

        private List<KeyWord> GetResumeKeyWords(string resumeFilePath)
        {
            return _wordReaderService
                .ReadWords(resumeFilePath)
                .ToList();
        }
    }
}