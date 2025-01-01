import sys
sys.path.append(r"python-workspace\src")
from word import Word, Importance

def test_word_initialization():
    word = Word("example", frequency=5, is_matched=True, importance=Importance.HIGH)
    assert word.word == "example"
    assert word.frequency == 5
    assert word.is_matched is True
    assert word.importance == Importance.HIGH

def test_word_repr():
    word = Word("example", 5, True, Importance.HIGH)
    assert repr(word) == "Word(word='example', frequency=5, is_matched=True, importance=Importance.HIGH)"

def test_word_str():
    word = Word("example", 5, True, Importance.HIGH)
    assert str(word) == "'example': Frequency=5, Matched=True, Importance=high"