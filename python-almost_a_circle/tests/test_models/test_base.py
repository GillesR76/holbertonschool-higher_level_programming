# test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_id_is_not_none(self):
        test1 = Base(12)
        self.assertEqual(test1.id, 12)
        
    def test_id_is_none(self):
        test2 = Base()
        test3 = Base()
        test4 = Base()
        self.assertEqual(test2.id, 1)
        self.assertEqual(test3.id, 2)
        self.assertEqual(test4.id, 3)

    