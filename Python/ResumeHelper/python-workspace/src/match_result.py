import os
from word import Importance

class MatchResult:
    def __init__(self, job_description, resume, match_score):
        self.job_description = job_description
        self.resume = resume
        self.match_score = match_score

    @property
    def statistics(self):
        stats = {
            Importance.HIGH: {'matched': 0, 'unmatched': 0},
            Importance.MEDIUM: {'matched': 0, 'unmatched': 0}
        }
        
        for word in self.job_description.words:
            if word.importance in stats:
                status = 'matched' if word.is_matched else 'unmatched'
                stats[word.importance][status] += 1
        
        return stats

    def __repr__(self):
        return (f"MatchResult(job_description_file='{self.job_description.file_path}', "
            f"resume_file='{self.resume.file_path}', "
            f"match_score={self.match_score:.2f})")
    
    def __str__(self):
        resume_filename = os.path.basename(self.resume.file_path)
        return (f"Resume: {resume_filename}\n"
            f"Match Score: {self.match_score:.2f}")
    
if __name__ == '__main__':
    from file_handler import FileHandler
    from resume_analyser import ResumeAnalyser
    file_handler = FileHandler(r"input_files")
    job_description_file, resume_file = next(file_handler.discover())
    analyser = ResumeAnalyser()
    match_result = analyser.analyse(job_description_file, resume_file)
    print(match_result)