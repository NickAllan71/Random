import sys
sys.path.append(r"python-workspace\src")
import pytest
from resume_analyser import ResumeAnalyser
from word import Word, Importance
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_job_description():
    job_desc = MagicMock()
    job_desc.words = [
        Word("Python", 2, True, Importance.HIGH),
        Word("SQL", 1, True, Importance.MEDIUM),
        Word("Java", 1, False, Importance.LOW)
    ]
    return job_desc

@pytest.fixture
def mock_resume():
    resume = MagicMock()
    resume.words = [
        Word("Python", 1, True, Importance.HIGH),
        Word("SQL", 1, True, Importance.MEDIUM),
        Word("C#", 1, False, Importance.LOW)
    ]
    return resume

def test_init():
    analyser = ResumeAnalyser(high_importance_weighting=2, low_importance_weighting=0.5)
    assert analyser.high_importance_weighting == 2
    assert analyser.low_importance_weighting == 0.5

@patch('resume_analyser.JobDescription')
@patch('resume_analyser.Resume')
def test_analyse(mock_resume_class, mock_jd_class, mock_job_description, mock_resume):
    mock_jd_class.return_value = mock_job_description
    mock_resume_class.return_value = mock_resume
    
    analyser = ResumeAnalyser(high_importance_weighting=1, low_importance_weighting=0.5)
    result = analyser.analyse("job.docx", "resume.docx")
    
    assert result is not None
    mock_resume.match.assert_called_once_with(mock_job_description)
    mock_job_description.match.assert_called_once_with(mock_resume)

def test_calculate_match_score(mock_job_description, mock_resume):
    analyser = ResumeAnalyser(high_importance_weighting=1, low_importance_weighting=0.5)
    score = analyser._calculate_match_score(mock_job_description, mock_resume)
    assert isinstance(score, float)
    assert 0 <= score <= 1