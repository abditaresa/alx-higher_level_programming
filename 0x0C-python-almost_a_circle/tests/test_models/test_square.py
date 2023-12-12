import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square_creation(self):
        s = Square(5)
        self.assertIsInstance(s, Square)
