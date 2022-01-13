import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase): 

    def setUp(self):
       self.guest1 = Guest("Ricardo", 50)
       self.guest2 = Guest("Antonia", 100)

    def test_can_create_guest(self):
        self.assertEqual("Antonia", self.guest2.name)