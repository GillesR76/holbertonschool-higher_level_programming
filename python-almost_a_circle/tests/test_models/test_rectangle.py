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
            
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2")
            
        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, "3")
            
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, "4")
        
        r8 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r8.width, 10)
        self.assertEqual(r8.height, 2)
        self.assertEqual(r8.x, 0)
        self.assertEqual(r8.y, 0)
        self.assertEqual(r8.id, 12)
        
        with self.assertRaises(ValueError):
            r9 = Rectangle(-1, 2)
            
        with self.assertRaises(ValueError):
            r10 = Rectangle(1, -2)
            
        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 2)
            
        with self.assertRaises(ValueError):
            r11 = Rectangle(1, 0)
            
        with self.assertRaises(ValueError):
            r12 = Rectangle(1, 2, -3)
            
        with self.assertRaises(ValueError):
            r13 = Rectangle(1, 2, 3, -4)
            
        
            
        
        