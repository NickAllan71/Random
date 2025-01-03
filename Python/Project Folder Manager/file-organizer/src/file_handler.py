import os
import fnmatch
import shutil

class FileHandler:
    def __init__(self, folder_path: str, file_spec: str):
        """Initialize with folder path and file specification pattern"""
        self.folder_path = folder_path
        self.file_spec = file_spec
        self._validate_paths()

    def _validate_paths(self) -> None:
        """Validate the folder path exists and is a directory"""
        if not os.path.exists(self.folder_path):
            raise ValueError(f"Folder path does not exist: {self.folder_path}")
        if not os.path.isdir(self.folder_path):
            raise ValueError(f"Path is not a directory: {self.folder_path}")

    def find_matching_files(self) -> list[str]:
        """Find all files matching the file specification pattern"""
        matching_files = []
        
        # Get all files in the root directory only
        for filename in os.listdir(self.folder_path):
            if os.path.isfile(os.path.join(self.folder_path, filename)) and fnmatch.fnmatch(filename, self.file_spec):
                matching_files.append(os.path.join(self.folder_path, filename))

        return matching_files

    def organize_files(self, matching_files: list[str]) -> None:
        """Move each file into a new directory named after the file"""
        for file_path in matching_files:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            new_folder_path = os.path.join(os.path.dirname(file_path), file_name)

            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)

            shutil.move(file_path, os.path.join(new_folder_path, os.path.basename(file_path)))

    def process(self) -> list[str]:
        """Main method to execute the file organization process"""
        matching_files = self.find_matching_files()
        if matching_files:
            self.organize_files(matching_files)
        return matching_files