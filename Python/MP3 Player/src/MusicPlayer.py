from queue import Queue

import vlc
from src.MusicLibrary import MusicLibrary
from src.Song import Song


class MusicPlayer:
    current_song: Song

    def __init__(self, library: MusicLibrary):
        self.player = None
        self.library = library
        self.play_list = []
        self.current_song = None
        self.play_list_length = 10

    def start(self):
        self.current_song = self.get_next_song()
        self.player = vlc.MediaPlayer(self.current_song.full_path)
        self.player.play()

    def get_next_song(self):
        if not self.play_list:
            self.play_list = self.library.get_random_playlist(self.play_list_length)

        return self.play_list.pop()

    def next(self):
        self.stop()
        self.start()

    def previous(self):
        self.stop()

    def stop(self):
        self.player.stop()
