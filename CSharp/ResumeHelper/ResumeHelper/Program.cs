using ResumeHelper.Factories;
using ResumeHelper.Services;

namespace ResumeHelper
{
    class Program
    {
        static string GetParameterFromUser(string parameterName, string[] args, int argIndex, string defaultValue)
        {
            
            var commandLineArg = args.Length > argIndex ? args[argIndex] : null;

            Console.Write($"{parameterName}");

            if (commandLineArg != null)
            {
                Console.WriteLine($": {commandLineArg}");
                return commandLineArg;
            }

            Console.Write($" <{defaultValue}>: ");
            var input = Console.ReadLine();

            return string.IsNullOrWhiteSpace(input) ? defaultValue : input;
        }

        static void Main(string[] args)
        {
            var rootFolderPath = GetParameterFromUser("Root Folder Path", args, 0, ".");
            var recursive = bool.Parse(GetParameterFromUser("Recursive", args, 1, "false"));

            Console.WriteLine($"Root Folder Path: {rootFolderPath}");
            Console.WriteLine($"Recursive: {recursive}");

            var fileHandler = new FileHandlerService();
            var jobDescriptionFilePath = fileHandler.Discover(
                rootFolderPath, "*Job*Desc*.docx", recursive)
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
                    Console.ForegroundColor = keyWord.ForegroundColor;
                    Console.BackgroundColor = keyWord.BackgroundColor;
                    Console.Write($"{keyWord}");
                    Console.ResetColor();
                    Console.Write(" ");
                }
                Console.WriteLine();
            }
        }
    }
}