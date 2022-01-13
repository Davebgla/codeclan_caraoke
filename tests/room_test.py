import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
       self.room1 = Room("Blue Room")
       self.room2 = Room("Green Room")
       self.room_list = [self.room1, self.room2]
       self.guest1 = Guest("Ricardo", 50)
       self.guest2 = Guest("Antonia", 100)
       self.guest_list = [self.guest1, self.guest2]

    
    def test_can_create_room(self):
        self.assertEqual("Blue Room", self.room1.name )

    def test_can_check_in_guest_to_room(self):
        self.room1.check_in_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room1.capacity))