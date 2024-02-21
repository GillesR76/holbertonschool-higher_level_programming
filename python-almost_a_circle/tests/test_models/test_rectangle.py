# test_rectangle.py

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    
    def test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        
        r2 = Rectangle(10, 2, 0)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 0)
        
        r3 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        
        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)
        
        r8 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r8.width, 10)
        self.assertEqual(r8.height, 2)
        self.assertEqual(r8.x, 0)
        self.assertEqual(r8.y, 0)
        self.assertEqual(r8.id, 12)
        