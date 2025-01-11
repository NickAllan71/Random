using ResumeHelper.Domain;
using ResumeHelper.Factories;
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
            var resumeMatchingService = ResumeMatchingServiceFactory.Build();
            foreach(var resumeFile in resumeFilePaths)
            {
                Console.WriteLine($"Resume File: {resumeFile}");
                var match = resumeMatchingService.Match(resumeFile, jobDescriptionFilePath);
                foreach(var keyWord in match.KeyWords)
                {
                    var colour = GetColour(keyWord);
                    Console.ForegroundColor = keyWord.IsMatch ? ConsoleColor.White : colour;
                    Console.BackgroundColor = keyWord.IsMatch ? colour : ConsoleColor.Black;
                    Console.Write($"{keyWord}");
                    Console.ResetColor();
                    Console.Write(" ");
                }
                Console.WriteLine();
            }
        }

        private static ConsoleColor GetColour(KeyWord keyWord)
        {
            return keyWord.Importance switch
            {
                KeywordImportance.High => ConsoleColor.Red,
                KeywordImportance.Medium => ConsoleColor.Green,
                KeywordImportance.Low => ConsoleColor.DarkGray,
                _ => ConsoleColor.DarkGray
            };
        }
    }
}