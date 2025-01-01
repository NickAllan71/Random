# Python Workspace for Job Description and Resume Processing

This project provides a set of classes to read and process job descriptions and resumes from Word documents (.docx). It includes functionality to extract words and identify their attributes.

## Project Structure

```
python-workspace
├── src
│   ├── __init__.py
│   ├── word_reader.py
│   ├── job_description.py
│   ├── resume.py
│   ├── word.py
│   └── base_document.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, ensure you have Python installed. Then, install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **WordReader**: Use this class to open and read the text of a Word document. It can also return highlighted words of a specified color.

2. **JobDescription**: Initialize this class with the file path of a job description in .docx format. Use its method to retrieve words as instances of the `Word` class.

3. **Resume**: Similar to `JobDescription`, this class initializes with a file path and provides a method to return words as instances of the `Word` class.

4. **Word**: This class represents a word with attributes indicating its importance, frequency, and whether it matches a certain criteria.

## Example

```python
from src.word_reader import WordReader
from src.job_description import JobDescription
from src.resume import Resume

# Example usage
word_reader = WordReader("path/to/document.docx")
highlighted_words = word_reader.get_highlighted_words("yellow")

job_description = JobDescription("path/to/job_description.docx")
job_words = job_description.get_words()

resume = Resume("path/to/resume.docx")
resume_words = resume.get_words()
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.