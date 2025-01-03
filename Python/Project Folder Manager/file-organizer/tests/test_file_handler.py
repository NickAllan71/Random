import sys
sys.path.append(r"file-organizer\src")
import os
import pytest
import tempfile
from file_handler import FileHandler

def create_test_files(temp_dir, files_dict):
    """Helper to create test files"""
    created_files = []
    for filename, content in files_dict.items():
        file_path = os.path.join(temp_dir, filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)
        created_files.append(file_path)
    return created_files

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as td:
        yield td

def test_find_exact_file(temp_dir):
    files = create_test_files(temp_dir, {"test.txt": "test"})
    organizer = FileHandler(temp_dir, "test.txt")
    found = organizer.find_matching_files()
    assert len(found) == 1
    assert os.path.basename(found[0]) == "test.txt"

def test_find_wildcard_pattern(temp_dir):
    create_test_files(temp_dir, {
        "test1.txt": "content",
        "test2.txt": "content",
        "other.doc": "content"
    })
    organizer = FileHandler(temp_dir, "*.txt")
    found = organizer.find_matching_files()
    assert len(found) == 2
    assert all(f.endswith('.txt') for f in found)

def test_invalid_directory():
    with pytest.raises(ValueError):
        FileHandler("nonexistent_dir", "*.txt")

def test_process_files(temp_dir):
    files = create_test_files(temp_dir, {"test.txt": "content"})
    organizer = FileHandler(temp_dir, "*.txt")
    processed = organizer.process()
    
    # Check file was moved to new directory
    assert len(processed) == 1
    new_dir = os.path.join(temp_dir, "test")
    assert os.path.isdir(new_dir)
    assert os.path.exists(os.path.join(new_dir, "test.txt"))