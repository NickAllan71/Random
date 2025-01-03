# README.md

# File Organizer Utility

The File Organizer is a Python utility designed to help users organize files in a specified folder. It takes command-line arguments to specify the folder path and file specifications, allowing for efficient file management.

## Features

- Searches for files matching a specified pattern in a given folder.
- Removes file extensions and organizes files into newly created directories named after the files.

## Usage

To run the utility, use the following command:

```
python src/main.py <FolderPath> <FileSpec>
```

Replace `<FolderPath>` with the path to the folder you want to organize and `<FileSpec>` with the file specification (e.g., `*.txt`).

## Testing

To run the tests, use:

```
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
