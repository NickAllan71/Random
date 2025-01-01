from base_document import BaseDocument
from word import Importance
from colour_code import ColourCode

class KeywordVisualiser:
    def __init__(self, document: BaseDocument):
        if not isinstance(document, BaseDocument):
            raise TypeError("document must be an instance of BaseDocument")
        self.document = document

    def print_word(self, word):
        colour_code = ColourCode(word.is_matched, word.importance)
        colour_code.print(word.word, end="\t")

    def visualise(self):
        self.document.sort()

        print("\nKeywords and Their Importance (excluding LOW):")
        for word in self.document.words:
            if word.importance != Importance.LOW:
                self.print_word(word)
        print() 

    def print_legend(self):
        print("Legend:")        
        for importance in [Importance.HIGH, Importance.MEDIUM]:
            for is_matched in [True, False]:
                colour_code = ColourCode(is_matched, importance)
                colour_code.print(f"\t{colour_code}") # Newline at the end

if __name__ == '__main__':
    from resume_analyser import ResumeAnalyser
    from file_handler import FileHandler

    file_handler = FileHandler(r"input_files")
    for job_description_file, resume_file in file_handler.discover():
        analyser = ResumeAnalyser()
        result = analyser.analyse(job_description_file, resume_file)
        print(result)
        visualiser = KeywordVisualiser(result.job_description)
        visualiser.print_legend()
        visualiser.visualise()