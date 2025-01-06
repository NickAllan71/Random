from base_document import BaseDocument
from word import Importance

class JobDescription(BaseDocument):
    def __init__(self, file_path, unimportant_words_path):
        super().__init__(file_path, unimportant_words_path)

    def get_words(self):
        return super().get_words()

    def get_importance(self, word: str) -> Importance:
        lower_word = word.lower()
        if lower_word in self.unimportant_words:
            return Importance.LOW
        if lower_word in (highlighted_word.lower() for highlighted_word in self.highlighted_words):
            return Importance.HIGH
        return Importance.MEDIUM

if __name__ == '__main__':
    job_description = JobDescription(
        r"C:\Users\Nick\Dropbox\Job Hunting\Applications\In Progress\Systems Developer- Identity Access Management\Job Description.docx",
        r"input_files\unimportant_words.txt"
    )
    print(job_description)
    print(job_description.highlighted_words)