using System;

namespace ResumeHelper.Domain;

public class KeyWord
{
    public readonly string Word;
    public EnumKeywordImportance Importance { get; set; }

    public KeyWord(string word)
    {
        Word = word;
    }
}
