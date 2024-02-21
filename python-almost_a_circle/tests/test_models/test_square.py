# test_square.py

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square(self):
        r1 = Square(1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 2)
