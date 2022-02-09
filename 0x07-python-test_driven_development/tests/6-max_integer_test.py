#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
from parameterized import parameterized

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([45, 1, 3, 12]), 45)

    def test_max_integer_1(self):
        self.assertEqual(max_integer([45, 1, 200, 3, 12]), 200)
    
    def test_max_integer_2(self):
        self.assertEqual(max_integer([45, 1, 3, 12, 200]), 200)
    
    def test_max_integer_3(self):
        self.assertEqual(max_integer([]), None)
    
    def test_max_integer_4(self):
        self.assertEqual(max_integer([45, 1, 3, -12]), 45)
    
    def test_max_integer_5(self):
        self.assertEqual(max_integer([-45, -1, -3, -12]), -1)
    
    def test_max_integer(self):
        self.assertEqual(max_integer([45]), 45)
    
