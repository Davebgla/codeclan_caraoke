import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase): 

    def setUp(self):
       self.guest1 = Guest("Ricardo", 50)
       self.guest2 = Guest("Antonia", 100)
       self.guest3 = Guest("Dario", 0)

    def test_guest_has_name(self):
        self.assertEqual("Antonia", self.guest2.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)










