# test_square.py

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_square(self):
        s1 = Square(1, 2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        
        with self.assertRaises(TypeError):
            r4 = Square("1", 2)
