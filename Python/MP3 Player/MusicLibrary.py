import os
import random


class MusicLibrary:
    def __init__(self, root_path, max_length=1000):
        self.songs = []
        for folder, subfolder_list, file_list in os.walk(root_path):
            for file in file_list:
                filename, file_extension = os.path.splitext(file)
                if file_extension == ".mp3":
                    self.songs.append(os.path.join(folder, file))
                    if len(self.songs) == max_length:
                        return

    def get_random_playlist(self, length):
        return random.sample(self.songs, length)
