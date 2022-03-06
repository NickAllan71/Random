from src.MusicLibrary import MusicLibrary
from src.MusicPlayer import MusicPlayer

first_song = "1st"
second_song = "2nd"
third_song = "3rd"


def create_sut():
    library = MusicLibrary("\\\\nicksnas\\Public\\Shared Music\\")

    sut = MusicPlayer(library)
    sut.play_list = [first_song, second_song, third_song]

    return sut


def test_get_next_song():
    sut = create_sut()

    assert sut._get_next_song() == first_song
    assert sut._get_next_song() == second_song
    assert sut._get_next_song() == third_song
    assert sut._get_next_song() is None


def test_get_previous_song():
    sut = create_sut()
    assert sut._get_next_song() == first_song
    assert sut._get_next_song() == second_song
    assert sut._get_previous_song() == first_song
    assert sut._get_previous_song() is None


def test_next_then_previous_song():
    sut = create_sut()
    assert sut._get_next_song() == first_song
    assert sut._get_next_song() == second_song
    assert sut._get_next_song() == third_song
    assert sut._get_previous_song() == second_song
    assert sut._get_previous_song() == first_song
