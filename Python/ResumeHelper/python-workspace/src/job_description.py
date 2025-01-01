from base_document import BaseDocument
from word import Importance

class JobDescription(BaseDocument):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_words(self):
        return super().get_words()

    def get_importance(self, word: str) -> Importance:
        # Check if the word is highlighted
        if word.lower() in (highlighted_word.lower() for highlighted_word in self.highlighted_words):
            return Importance.HIGH
        
        # Use the base class logic for other cases
        return super().get_importance(word)

if __name__ == '__main__':
    from file_handler import FileHandler
    file_handler = FileHandler(r"input_files")
    for job_description_file, _ in file_handler.discover():
        job_description = JobDescription(job_description_file)
        words = job_description.words
        print('\n'.join(str(word) for word in words))