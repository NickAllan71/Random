import sys
sys.path.append(r"python-workspace\src")
import pytest
from job_description import JobDescription
from word import Word, Importance
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_base_document():
    with patch('job_description.BaseDocument') as mock:
        instance = mock.return_value
        instance.highlighted_words = ["Python", "SQL"]
        instance.get_importance.return_value = Importance.MEDIUM
        instance.get_words.return_value = [
            Word("Python", 1, True, Importance.HIGH),
            Word("developer", 1, True, Importance.MEDIUM)
        ]
        yield instance

def test_initialization():
    with patch('job_description.BaseDocument'):
        job_desc = JobDescription("test_path")
        assert isinstance(job_desc, JobDescription)

def test_get_words():
    job_desc = create_SUT()
    words = job_desc.get_words()
    assert len(words) == 3
    assert words[0].word == "We"
    assert words[1].word == "need"
    assert words[2].word == "you"

def create_SUT():
    return JobDescription(r"python-workspace\tests\integration_test_files\Test_Job_Description.docx")

def test_get_importance_highlighted():
    job_desc = create_SUT()
    last_word = job_desc.get_words()[2]
    assert last_word.frequency == 1
    assert last_word.is_matched == False
    assert last_word.importance == Importance.LOW