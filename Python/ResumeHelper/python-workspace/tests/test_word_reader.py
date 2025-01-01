import sys
sys.path.append(r"python-workspace\src")
import pytest
from word_reader import WordReader
from docx import Document
from unittest.mock import MagicMock

@pytest.fixture
def mock_document(mocker):
    mock_doc = MagicMock(spec=Document)
    mock_doc.paragraphs = [MagicMock(text="Paragraph 1"), MagicMock(text="Paragraph 2")]
    mock_table = MagicMock()
    mock_table.rows = [
        MagicMock(cells=[MagicMock(text="Cell 1"), MagicMock(text="Cell 2")]),
        MagicMock(cells=[MagicMock(text="Cell 3"), MagicMock(text="Cell 4")])
    ]
    mock_doc.tables = [mock_table]
    mocker.patch('word_reader.Document', return_value=mock_doc)
    return mock_doc

def test_read_paragraphs(mock_document):
    reader = WordReader("dummy_path")
    result = reader.read_paragraphs()
    assert result == "Paragraph 1\nParagraph 2"

def test_read_tables(mock_document):
    reader = WordReader("dummy_path")
    result = reader.read_tables()
    assert result == "Cell 1\nCell 2\nCell 3\nCell 4"