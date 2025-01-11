using ResumeHelper.Services;

namespace ResumeHelper
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length < 2)
            {
                Console.WriteLine("Usage: ResumeHelper <rootFolderPath> <recursive>");
                return;
            }

            string rootFolderPath = args[0];
            bool recursive = bool.Parse(args[1]);

            Console.WriteLine($"Root Folder Path: {rootFolderPath}");
            Console.WriteLine($"Recursive: {recursive}");

            var fileHandler = new FileHandlerService();
            var jobDescriptionFilePath = fileHandler.Discover(
                rootFolderPath, "*JobDescription*.docx", recursive)
                .Single();
            
            Console.WriteLine($"Job Description File: {jobDescriptionFilePath}");
            
            var resumeFilePaths = fileHandler.Discover(rootFolderPath, "*Resume*.docx", recursive);
            foreach(var resumeFile in resumeFilePaths)
            {
                Console.WriteLine($"Resume File: {resumeFile}");
                //var resumeHelper = new ResumeHelper(wordReaderService);
            }
        }
    }
}