import sys
sys.path.append(r"python-workspace\src")
import pytest
from resume import Resume
from base_document import BaseDocument
from word import Word, Importance
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_base_document():
    mock_doc = MagicMock(spec=BaseDocument)
    mock_doc.words = [
        Word("Python", 1, True, Importance.HIGH),
        Word("Data", 1, True, Importance.MEDIUM),
        Word("Engineer", 1, False, Importance.LOW)
    ]
    mock_doc.unimportant_words = set(["the", "and", "is"])
    return mock_doc

def test_init(mock_base_document):
    resume = Resume("dummy_path")
    assert isinstance(resume, Resume)

def test_get_words(mock_base_document):
    with patch('resume.Resume.get_words') as mock_get_words:
        mock_get_words.return_value = mock_base_document.words
        resume = Resume("dummy_path")
        words = resume.get_words()
        assert len(words) == 3
        assert words[0].word == "Python"

def test_match(mock_base_document):
    resume = Resume("dummy_path")
    test_words = [
        Word("Python", 1, True, Importance.LOW),
        Word("Data", 1, True, Importance.LOW),
        Word("Engineer", 1, False, Importance.LOW)
    ]
    resume._words = test_words
    resume._unimportant_words = set(["the", "and", "is"])
    
    resume.match(mock_base_document)
    
    assert resume.words[0].importance == Importance.HIGH
    assert resume.words[1].importance == Importance.MEDIUM
    assert resume.words[2].importance == Importance.LOW