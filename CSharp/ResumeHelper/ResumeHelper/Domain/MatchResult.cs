namespace ResumeHelper.Domain;

public class MatchResult
{
    private List<KeyWord> _keyWords = [];

    public IEnumerable<KeyWord> KeyWords => _keyWords;

    public void AddKeyWord(KeyWord keyWord)
    {
        _keyWords.Add(keyWord);
    }
}