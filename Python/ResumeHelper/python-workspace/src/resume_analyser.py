from job_description import JobDescription
from resume import Resume
from word import Importance
from match_result import MatchResult

class ResumeAnalyser:
    def __init__(self, high_importance_weighting=1, low_importance_weighting=0):
        self.high_importance_weighting = high_importance_weighting
        self.low_importance_weighting = low_importance_weighting

    def analyse(self, job_description_file, resume_file):
        job_description = JobDescription(job_description_file)
        resume = Resume(resume_file)
        resume.match(job_description)
        job_description.match(resume)
        match_score = self._calculate_match_score(job_description, resume)
        return MatchResult(job_description, resume, match_score)

    def _calculate_match_score(self, job_description, resume):
        high_importance_score = self._calculate_weighted_score(job_description, resume, Importance.HIGH, self.high_importance_weighting)
        medium_importance_score = self._calculate_weighted_score(job_description, resume, Importance.MEDIUM, self.low_importance_weighting)
        total_score = high_importance_score + medium_importance_score
        return min(total_score, 1.0)

    def _calculate_weighted_score(self, job_description, resume, importance_level, weighting):
        required_words = self._get_words_by_importance(job_description, importance_level)
        matched_words = self._get_words_by_importance(resume, importance_level)
        if not required_words:
            return 0.0
        return (len(matched_words) / len(required_words)) * weighting
    
    def _get_words_by_importance(self, document, importance_level):
        return {word.word.lower() for word in document.words if word.importance == importance_level}


if __name__ == '__main__':
    job_description_file = r"input_files\Microsoft SQL DBA - La Fosse Job Description.docx"
    resume_file = r"input_files\Nick Allan's Resume A.docx"
    analyser = ResumeAnalyser()
    match_result = analyser.analyse(job_description_file, resume_file)
    print(match_result.resume.words)
    print(match_result)