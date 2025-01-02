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
    from file_handler import FileHandler
    file_handler = FileHandler(
        r"C:\Users\Nick\Dropbox\Job Hunting\Applications\In Progress\Brill Power (Oxford) - Travis Kennard",
        r"C:\Users\Nick\Dropbox\Job Hunting\Applications\Pending",
        recursive=True)
    
    job_description_file, _ = next(file_handler.discover())
    job_description = JobDescription(job_description_file)
    print(job_description)
    print(job_description.highlighted_words)