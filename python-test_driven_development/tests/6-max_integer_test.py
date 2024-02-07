#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 4, 8]), 8)
        self.assertEqual(max_integer([2, 9, 6, 7, 22]), 22)
        self.assertEqual(max_integer([-1, -5, -4]), -1)

if __name__ == '__main__': 
    unittest.main() 