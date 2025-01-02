import sys
sys.path.append(r"python-workspace\src")
import pytest
from file_handler import FileHandler
from unittest.mock import patch, MagicMock

@pytest.fixture
def temp_dir(tmp_path):
    # Create main folder files
    job_desc = tmp_path / "test job description.docx"
    resume1 = tmp_path / "Test Resume 1.docx"
    resume2 = tmp_path / "Test Resume 2.docx"
    
    job_desc.write_text("dummy content")
    resume1.write_text("dummy content")
    resume2.write_text("dummy content")
    
    # Create subfolder and files
    sub_dir = tmp_path / "subfolder"
    sub_dir.mkdir()
    
    resume3 = sub_dir / "Test Resume 3.docx"
    resume4 = sub_dir / "Test Resume 4.docx"
    temp_file = sub_dir / "~$temp.docx"
    
    resume3.write_text("dummy content")
    resume4.write_text("dummy content")
    temp_file.write_text("temp content")
    
    return tmp_path

def test_discover(temp_dir):
    handler = FileHandler(str(temp_dir))
    files = list(handler.discover())
    
    assert len(files) == 2
    for job_desc, resume in files:
        assert "job description" in job_desc.lower()
        assert "resume" in resume.lower()

def test_no_job_description(temp_dir):
    for f in temp_dir.glob("*job*"):
        f.unlink()
    
    handler = FileHandler(str(temp_dir))
    with pytest.raises(ValueError) as exc:
        list(handler.discover())
    assert "job description" in str(exc.value)

def test_no_resumes(temp_dir):
    for f in temp_dir.glob("*Resume*"):
        f.unlink()
    
    handler = FileHandler(str(temp_dir))
    with pytest.raises(ValueError) as exc:
        list(handler.discover())
    assert "resume" in str(exc.value)

@patch('file_handler.ResumeAnalyser')
def test_analyse(mock_analyser_class, temp_dir):
    mock_analyser = MagicMock()
    mock_analyser_class.return_value = mock_analyser
    mock_analyser.analyse.return_value = "test result"
    
    handler = FileHandler(str(temp_dir))
    results = list(handler.analyse())
    
    assert len(results) == 2
    assert all(result == "test result" for result in results)
    assert mock_analyser.analyse.call_count == 2

def test_multiple_job_descriptions(temp_dir):
    extra_job = temp_dir / "another job description.docx"
    extra_job.write_text("dummy content")
    
    handler = FileHandler(str(temp_dir))
    with pytest.raises(ValueError) as exc:
        list(handler.discover())
    assert "exactly one job description" in str(exc.value)

def test_recursive_search(temp_dir):
    handler = FileHandler(str(temp_dir), recursive=True)
    files = list(handler.discover())
    assert len(files) == 4  # 2 root + 2 subfolder resumes
    
    handler = FileHandler(str(temp_dir), recursive=False)
    files = list(handler.discover())
    assert len(files) == 2  # only root resumes