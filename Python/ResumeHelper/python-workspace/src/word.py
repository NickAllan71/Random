from enum import Enum

class Importance(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

class Word:
    def __init__(self, word: str, frequency: int, is_matched: bool, importance: Importance):
        self.word = word
        self.frequency = frequency
        self.is_matched = is_matched
        self.importance = importance

    def __repr__(self):
        return f"Word(word='{self.word}', frequency={self.frequency}, is_matched={self.is_matched}, importance={self.importance})"

    def __str__(self):
        return f"'{self.word}': Frequency={self.frequency}, Matched={self.is_matched}, Importance={self.importance.name.lower()}"
