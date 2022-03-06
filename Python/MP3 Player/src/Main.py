from MusicLibrary import MusicLibrary
from MusicPlayer import MusicPlayer

library = MusicLibrary("\\\\nicksnas\\Public\\Shared Music\\")
music_player = MusicPlayer(library)
music_player.start()

for song in range(200):
    music_player.next()
    print(music_player.current_song)
    input()

music_player.stop()
