import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room1 = Room("Blue Room")
       self.room2 = Room("Green Room")
       self.room_list = [self.room1, self.room2]
       self.guest1 = Guest("Ricardo", 50)
       self.guest2 = Guest("Antonia", 100)
       self.guest_list = [self.guest1, self.guest2]
       self.song1 = Song("Kind Of Blue")
       self.song2 = Song("Right Down The Line")
       self.song_list = [self.song1, self.song2]


    
    def test_can_create_room(self):
        self.assertEqual("Blue Room", self.room1.name)

    def test_check_in_guest(self):
        self.room1.check_in_guest(Guest)
        self.assertEqual(3, self.room1.guest_count())

    def test_check_out_guest(self):
        self.room1.check_out_guest(Guest)
        self.assertEqual(1, self.room1.guest_count())

    def test_can_add_song_to_room(self):
        self.room1.add_song(Song)
        self.assertEqual(3, self.room1.song_count())

    def test_room_is_full(self):
        self.room1.room_is_full
        self.assertEqual(2, self.room1.guest_count())



