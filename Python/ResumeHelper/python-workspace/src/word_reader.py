from docx import Document
from docx.enum.text import WD_COLOR_INDEX
import re

class WordReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.document = Document(file_path)

    def read_paragraphs(self):
        text = []
        for paragraph in self.document.paragraphs:
            text.append(paragraph.text)
        return '\n'.join(text)

    def read_tables(self):
        text = []
        for table in self.document.tables:
            for row in table.rows:
                for cell in row.cells:
                    text.append(cell.text)
        return '\n'.join(text)

    def get_highlighted_words(self, color=WD_COLOR_INDEX.YELLOW):
        highlighted_words = []
        for paragraph in self.document.paragraphs:
            for run in paragraph.runs:
                if run.font.highlight_color and run.font.highlight_color == color:
                    highlighted_words.extend(run.text.split())
        return highlighted_words

    def extract_words(self, text):
        for word in re.findall(r'\b[a-z]\w*\b', text, re.IGNORECASE):
            yield word

    def get_words(self):
        # Extract words from paragraphs
        yield from self.extract_words(self.read_paragraphs())
        # Extract words from tables
        yield from self.extract_words(self.read_tables())

if __name__ == '__main__':
    word_reader = WordReader(r"input_files\Microsoft SQL DBA - La Fosse Job Description.docx")
    print("\nHighlighted Words:")
    print(word_reader.get_highlighted_words())
    print("\nWords:")
    print(list(word_reader.get_words()))