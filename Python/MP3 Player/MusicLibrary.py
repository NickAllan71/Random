import os
import random
from Song import Song


class MusicLibrary:
    def __init__(self, root_path, max_length=100):
        self.songs = []
        for folder, subfolder_list, file_list in os.walk(root_path):
            for file in file_list:
                song = Song(folder, file)
                if not song.is_valid_format:
                    break

                self.songs.append(song)
                if len(self.songs) == max_length:
                    return

    def get_random_playlist(self, length):
        return random.sample(self.songs, length)
