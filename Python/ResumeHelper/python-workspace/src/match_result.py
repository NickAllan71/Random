import os

class MatchResult:
    def __init__(self, job_description, resume, match_score):
        self.job_description = job_description
        self.resume = resume
        self.match_score = match_score

    def __repr__(self):
        return (f"MatchResult(job_description_file='{self.job_description.file_path}', "
            f"resume_file='{self.resume.file_path}', "
            f"match_score={self.match_score:.2f})")
    
    def __str__(self):
        resume_filename = os.path.basename(self.resume.file_path)
        return (f"Resume: {resume_filename}\n"
                f"Match Score: {self.match_score:.2f}")