import os
import glob
from resume_analyser import ResumeAnalyser

class FileHandler:
    def __init__(self, 
                 job_description_folder, resume_folder=None, unimportant_words_file_path=None, recursive=False):
        self.job_description_folder = job_description_folder
        self.resume_folder = resume_folder or job_description_folder
        self.unimportant_words_file_path = unimportant_words_file_path or job_description_folder
        self.recursive = recursive

    def discover(self):
        job_description_file = self._find_file('*job desc*.docx', "job description", self.job_description_folder)
        resume_files = self._find_files('*Resume*.docx', "resume", self.resume_folder)        
        for resume_file in resume_files:
            yield job_description_file, resume_file

    def analyse(self):
        analyser = ResumeAnalyser(
            unimportant_words_file_path=self.unimportant_words_file_path)
        for job_description_file, resume_file in self.discover():
            result = analyser.analyse(job_description_file, resume_file)
            yield result

    def _find_file(self, file_pattern, file_description, folder):
        files = self._find_matching_files(file_pattern, folder)
        if len(files) != 1:
            raise ValueError(f"Expected exactly one {file_description} file, found {len(files)}: {files}")
        return files[0]

    def _find_files(self, file_pattern, file_description, folder):
        files = self._find_matching_files(file_pattern, folder)
        if not files:
            raise ValueError(f"Expected at least one {file_description} file, found {len(files)}: {files}")
        return files

    def _find_matching_files(self, file_pattern, folder):
        pattern = '**/' if self.recursive else ''
        full_pattern = os.path.join(folder, f'{pattern}{file_pattern}')
        matched_files = glob.glob(full_pattern, recursive=self.recursive)
        
        # Filter temp files and return full paths
        return [f for f in matched_files if not self._is_temp_file(f)]

    def _is_temp_file(self, filename):
        return os.path.basename(filename).startswith('~$')

if __name__ == '__main__':
    file_handler = FileHandler(r"input_files\multi_file_test", recursive=True)

    results = file_handler.discover()
    for job_description_file, resume_file in results:
        print(job_description_file, resume_file)