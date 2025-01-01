import sys
sys.path.append(r"python-workspace\src")
import pytest
from match_result import MatchResult
from unittest.mock import MagicMock

@pytest.fixture
def mock_documents():
    job_desc = MagicMock()
    job_desc.file_path = r"C:\jobs\test_job.docx"
    
    resume = MagicMock()
    resume.file_path = r"C:\resumes\test_resume.docx"
    
    return job_desc, resume

def test_init(mock_documents):
    job_desc, resume = mock_documents
    match_result = MatchResult(job_desc, resume, 0.75)
    assert match_result.job_description == job_desc
    assert match_result.resume == resume
    assert match_result.match_score == 0.75

def test_repr(mock_documents):
    job_desc, resume = mock_documents
    match_result = MatchResult(job_desc, resume, 0.75)
    expected = "MatchResult(job_description_file='C:\\jobs\\test_job.docx', resume_file='C:\\resumes\\test_resume.docx', match_score=0.75)"
    assert repr(match_result) == expected

def test_str(mock_documents):
    job_desc, resume = mock_documents
    match_result = MatchResult(job_desc, resume, 0.75)
    expected = "Resume: test_resume.docx\nMatch Score: 0.75"
    assert str(match_result) == expected

def test_match_score_rounding(mock_documents):
    job_desc, resume = mock_documents
    match_result = MatchResult(job_desc, resume, 0.7777777)
    assert "0.78" in str(match_result)