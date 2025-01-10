namespace ResumeHelper.Services;
using System.IO;

public class FileHandlerService
{
    public IEnumerable<string> Discover(
        string folderPath,
        string fileSpec="*.*",
        bool recursive=false)
    {
        var files = Directory.GetFiles(
            folderPath, fileSpec, getSearchOption(recursive));
        
        foreach (var file in files)
            yield return file;
    }

    static SearchOption getSearchOption(bool recursive)
    {
        return recursive ? SearchOption.AllDirectories : SearchOption.TopDirectoryOnly;
    }
}