from abc import ABC, abstractmethod
from word import Word, Importance
from word_reader import WordReader
from collections import Counter
from docx.enum.text import WD_COLOR_INDEX

class BaseDocument(ABC):
    def __init__(self, file_path, unimportant_words_path):
        self.file_path = file_path
        self.unimportant_words_path = unimportant_words_path
        self._words = None
        self._highlighted_words = None
        self._unimportant_words = None

    @property
    def unimportant_words(self):
        if self._unimportant_words is None:
            with open(self.unimportant_words_path, 'r') as file:
                self._unimportant_words = set(file.read().splitlines())
        return self._unimportant_words

    @property
    def words(self):
        if self._words is None:
            self._words = self.get_words()
        return self._words

    @property
    def highlighted_words(self):
        if self._highlighted_words is None:
            word_reader = self._create_word_reader()
            self._highlighted_words = list(word_reader.get_highlighted_words(WD_COLOR_INDEX.YELLOW))
        return self._highlighted_words

    def sort(self, reverse=True):
        def sort_key(word):
            # Map importance to numeric value for sorting
            importance_value = {
                Importance.HIGH: 2,
                Importance.MEDIUM: 1,
                Importance.LOW: 0
            }
            return (importance_value[word.importance], word.is_matched, word.frequency)

        self.words.sort(key=sort_key, reverse=reverse)

    @abstractmethod
    def get_words(self):
        words = []
        word_counter = Counter()

        word_reader = self._create_word_reader()
        for word in word_reader.get_words():
            word_counter[word] += 1

        for word, freq in word_counter.items():
            importance = self.get_importance(word)
            words.append(Word(word, frequency=freq, is_matched=False, importance=importance))
        
        return words

    def get_importance(self, word: str) -> Importance:
        if word.lower() in self.unimportant_words:
            return Importance.LOW
        return Importance.MEDIUM

    def match(self, other_document: 'BaseDocument'):
        other_words = {word.word.lower() for word in other_document.words}
        for word in self.words:
            if word.word.lower() in other_words:
                word.is_matched = True

    def _create_word_reader(self):
        return WordReader(self.file_path)

    def __repr__(self):
        return f"<{self.__class__.__name__} file_path={self.file_path}>"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.file_path}"