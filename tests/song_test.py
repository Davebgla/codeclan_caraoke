import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
       self.song1 = Song("Kind Of Blue")
       self.song2 = Song("Right Down The Line")

    def test_song_has_name(self):
        self.assertEqual("Kind Of Blue", self.song1.track)