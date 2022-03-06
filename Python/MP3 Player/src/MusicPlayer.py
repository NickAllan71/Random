from queue import Queue

import vlc
from src.MusicLibrary import MusicLibrary
from src.Song import Song


class MusicPlayer:
    current_song: Song

    def __init__(self, library: MusicLibrary):
        self._media_player = None
        self._library = library
        self.play_list = []
        self._next_song_index = None
        self.current_song = None
        self.play_list_length = 10

    def start(self):
        if not self.play_list:
            self.play_list = self._library.get_random_playlist(self.play_list_length)
        self.next()

    def stop(self):
        self._media_player.stop()

    def next(self):
        self.current_song = self._get_next_song()
        self._media_player = vlc.MediaPlayer(self.current_song.full_path)
        self._media_player.play()

    def previous(self):
        self.current_song = self._get_previous_song()
        self._media_player = vlc.MediaPlayer(self.current_song.full_path)
        self._media_player.play()

    def _get_next_song(self):
        if self._next_song_index is None:
            self._next_song_index = 0
        elif self._next_song_index == len(self.play_list) - 1:
            self._next_song_index = None
            return None
        else:
            self._next_song_index += 1

        next_song = self.play_list[self._next_song_index]
        return next_song

    def _get_previous_song(self):
        if self._next_song_index == 0:
            self._next_song_index = None
            return None

        self._next_song_index -= 1
        print(self._next_song_index)
        previous_song = self.play_list[self._next_song_index]
        return previous_song
