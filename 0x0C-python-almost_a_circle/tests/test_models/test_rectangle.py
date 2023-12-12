import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(10, 5)
        self.assertIsInstance(r, Rectangle)
