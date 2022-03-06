from src.Song import Song


def create_sut():
    return Song("\\\\nicksnas\\Public\\Shared Music\\10,000 Maniacs\\In My Tribe", "01 What's the Matter Here-.mp3")


def test_title():
    sut = create_sut()
    assert sut.title == "What's the Matter Here?"


def test_duration_seconds():
    sut = create_sut()
    assert sut.duration_seconds == 291.1608163265306
