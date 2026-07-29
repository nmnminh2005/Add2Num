# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:56:49 2026

@author: Owner
"""


import unittest
from my_big_number import MyBigNumber


class TestMyBigNumber(unittest.TestCase):

    def setUp(self):
        self.calculator = MyBigNumber()

    def test_normal_addition(self):
        self.assertEqual(
            self.calculator.sum("1234", "897"),
            "2131"
        )

    def test_addition_with_carry(self):
        self.assertEqual(
            self.calculator.sum("999", "2"),
            "1001"
        )

    def test_zero(self):
        self.assertEqual(
            self.calculator.sum("0", "0"),
            "0"
        )

    def test_different_lengths(self):
        self.assertEqual(
            self.calculator.sum("12345", "5"),
            "12350"
        )

    def test_large_numbers(self):
        self.assertEqual(
            self.calculator.sum("999999999999999999", "1"),
            "1000000000000000000"
        )


if __name__ == "__main__":
    unittest.main()