import os
from tinytag import TinyTag


class Song:
    def __init__(self, folder, file):
        self.folder = folder
        self.file = file
        self._tag = None
        self._supported_file_types = [".mp3", ".wma"]

    @property
    def is_valid_format(self):
        filename, file_extension = os.path.splitext(self.file)
        return file_extension in self._supported_file_types

    @property
    def full_path(self):
        return os.path.join(self.folder, self.file)

    @property
    def title(self):
        return self.tag.title

    @property
    def artist(self):
        return self.tag.artist

    @property
    def album(self):
        return self.tag.album

    @property
    def duration_seconds(self):
        return self.tag.duration

    @property
    def tag(self):
        if not self._tag:
            self._tag = TinyTag.get(self.full_path)
        return self._tag

    def __str__(self):
        if not self.is_valid_format:
            print("Unsupported file type")

        return f'"{self.title}" by {self.artist}, {self.album}'
