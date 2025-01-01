import os
import glob
from resume_analyser import ResumeAnalyser

class FileHandler:
    def __init__(self, folder_name):
        self.folder_name = folder_name

    def discover(self):
        job_description_file = self._find_file('*job desc*.docx', "job description")
        resume_files = self._find_files('*Resume*.docx', "resume")        
        for resume_file in resume_files:
            yield job_description_file, resume_file

    def analyse(self):
        analyser = ResumeAnalyser()
        for job_description_file, resume_file in self.discover():
            result = analyser.analyse(job_description_file, resume_file)
            yield result
    
    def _find_file(self, file_pattern, file_description):
        full_pattern = os.path.join(self.folder_name, file_pattern)
        files = glob.glob(full_pattern)
        if len(files) != 1:
            raise ValueError(f"Expected exactly one {file_description} file, found {len(files)}: {files}")
        return files[0]

    def _find_files(self, file_pattern, file_description):
        full_pattern = os.path.join(self.folder_name, file_pattern)
        files = glob.glob(full_pattern)
        if not files:
            raise ValueError(f"Expected at least one {file_description} file, found {len(files)}: {files}")
        return files

if __name__ == '__main__':
    from keyword_visualiser import KeywordVisualiser

    file_handler = FileHandler(r"input_files\multi_file_test")

    results = file_handler.analyse()
    sorted_results = sorted(results, key=lambda x: x.match_score, reverse=True)

    best_result = sorted_results[0]
    print(best_result.job_description)
    for result in sorted_results:
        print(result)

    print(f"Best match: {best_result}")
    visualiser = KeywordVisualiser(best_result.job_description)
    visualiser.print_legend()
    visualiser.visualise()