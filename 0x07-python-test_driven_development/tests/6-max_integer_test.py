#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
from parameterized import parameterized

class TestMaxInteger(unittest.TestCase):
    @parameterized.expand([
    ([45, 1, 3, 12], 45),
    ([1, 1, 1, 1], 1),
    ([], None)
   ])
    def test_max_integer(self, integers, expected):
        self.assertEqual(max_integer(integers), expected)

