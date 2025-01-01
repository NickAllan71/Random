from base_document import BaseDocument

class Resume(BaseDocument):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_words(self):
        return super().get_words()

    def match(self, other_document: BaseDocument):
        super().match(other_document)
        other_words_dict = {word.word.lower(): word.importance for word in other_document.words}
        for word in self.words:
            if word.word.lower() in self.unimportant_words:
                continue
            if word.is_matched and word.word.lower() in other_words_dict:
                word.importance = other_words_dict[word.word.lower()]

if __name__ == '__main__':
    from job_description import JobDescription
    resume = Resume(r"input_files\Nick Allan's Resume A.docx")
    job_description = JobDescription(r'input_files\Microsoft SQL DBA - La Fosse Job Description.docx')
    resume.match(job_description)
    words = resume.words
    print('\n'.join(str(word) for word in words))