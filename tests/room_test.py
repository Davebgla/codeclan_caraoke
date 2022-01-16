import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
       self.room = Room("Blue Room", 5, 10)
       self.guest1 = Guest("Ricardo", 50)
       self.guest2 = Guest("Antonia", 100)
       self.song1 = Song("Girls Just Wanna Have Fun")
       self.song2 = Song("Right Down The Line")

      


    def test_room_has_name(self):
        self.assertEqual("Blue Room", self.room.name)

    def test_room_starts_empty(self):
        self.assertEqual(0, self.room.guest_count())

    def test_can_check_in_to_room(self):
        guest = Guest("Ricardo", 50)
        self.room.add_guest(guest)
        self.assertEqual(1, self.room.guest_count())

    def test_guest_can_check_out_of_room(self):
        guest = Guest("Ricardo", 50)
        self.room.add_guest(guest)
        self.room.remove_guest(guest)
        self.assertEqual(0, self.room.guest_count())

    def test_song_list_starts_empty(self):
        self.assertEqual(0, self.room.song_count())

    def test_can_add_song_room(self):
        song = Song("Right Down The Line")
        self.room.add_song(song)
        self.assertEqual(1, self.room.song_count())









  

    
 
















        


