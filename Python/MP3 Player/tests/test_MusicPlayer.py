from src.MusicLibrary import MusicLibrary
from src.MusicPlayer import MusicPlayer


def create_sut():
    library = MusicLibrary("\\\\nicksnas\\Public\\Shared Music\\")
    return MusicPlayer(library)


def test_get_next_song():
    sut = create_sut()
    assert sut.get_next_song()
