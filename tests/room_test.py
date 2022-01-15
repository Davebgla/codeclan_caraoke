import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room1 = Room("Blue Room", 6, 5)
       self.room2 = Room("Green Room", 6, 5)
       self.room_list = [self.room1, self.room2]
       self.guest1 = Guest("Ricardo", 50)
       self.guest2 = Guest("Antonia", 100)
       self.guest_list = [self.guest1, self.guest2]
       self.song1 = Song("Kind Of Blue")
       self.song2 = Song("Right Down The Line")
       self.song_list = [self.song1, self.song2]
      

    def test_room_has_name(self):
        self.assertEqual("Blue Room", self.room1.name)

    def test_room_has_capacity(self):
        self.assertEqual(6, self.room2.capacity)

    def test_check_in(self):
        self.room2.check_in(self.guest1)
        self.assertEqual(1, len(self.room2.guests_in_room))

    def guest_check_out(self):
        self.room2.check_out(self.guest2)
        self.assertEqual(0, len(self.room2.guests_in_room))

    def test_add_song(self):
        self.room2.add_song(self.song2)
        self.assertEqual(1, len(self.room2.song_choice))















        


