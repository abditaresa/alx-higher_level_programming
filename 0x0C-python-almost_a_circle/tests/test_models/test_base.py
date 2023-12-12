import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base_creation(self):
        b = Base()
        self.assertIsInstance(b, Base)
