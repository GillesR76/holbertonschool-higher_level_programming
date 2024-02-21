# test_square.py

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_square(self):
        s1 = Square(1, 2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)

        s2 = Square(10, 2, 0)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(10, 2, 0, 0)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 0)
        self.assertEqual(s3.id, 0)

        with self.assertRaises(TypeError):
            s4 = Square("1", 2)

        with self.assertRaises(TypeError):
            s5 = Square(1, "2")

        with self.assertRaises(TypeError):
            s6 = Square(1, 2, "3")

        s8 = Square(10, 2, 0, 12)
        self.assertEqual(s8.size, 10)
        self.assertEqual(s8.x, 2)
        self.assertEqual(s8.y, 0)
        self.assertEqual(s8.id, 12)

        with self.assertRaises(ValueError):
            s9 = Square(-1, 2)

        with self.assertRaises(ValueError):
            s10 = Square(1, -2)

        with self.assertRaises(ValueError):
            s11 = Square(0, 2)

        with self.assertRaises(ValueError):
            r12 = Square(1, 2, -3)

        s9 = Square(1)
        self.assertEqual(s9.size, 1)

    def test_str(self):
        """Test the string method"""
        s1 = Square(3, 1, 3)
        self.assertEqual(s1.__str__(), "[Square] (11) 1/3 - 3")
