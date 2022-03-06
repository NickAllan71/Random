import os
from logging import getLogger
import eyed3


class Song:
    def __init__(self, folder, file):
        self._album = None
        self.folder = folder
        self.file = file
        self._title = None
        self._artist = None
        self._is_tag_read = False
        self._supported_file_types = [".mp3"]

    @property
    def is_valid_format(self):
        filename, file_extension = os.path.splitext(self.file)
        return file_extension in self._supported_file_types

    @property
    def full_path(self):
        return os.path.join(self.folder, self.file)

    @property
    def title(self):
        self.read_tag()
        return self._title

    @property
    def artist(self):
        self.read_tag()
        return self._artist

    @property
    def album(self):
        self.read_tag()
        return self._album

    def read_tag(self):
        if self._is_tag_read:
            return
        getLogger().setLevel('ERROR')
        audio_file = eyed3.load(self.full_path)
        tag = audio_file.tag
        self._title = tag.title
        self._artist = tag.artist
        self._album = tag.album

    def __str__(self):
        if not self.is_valid_format:
            print("Unsupported file type")

        return f'"{self.title}" by {self.artist}, {self.album}\n{self.file}'
