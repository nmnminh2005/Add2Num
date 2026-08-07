import unittest
import logging
from my_big_number import MyBigNumber

# Disable logging output during unit testing to keep logs clean
logging.disable(logging.CRITICAL)

class TestMyBigNumber(unittest.TestCase):
    def setUp(self):
        self.calculator = MyBigNumber()

    def test_example_from_requirement(self):
        # Sample test case from thầy Thạch Lê's requirement PDF: sum("1234", "897") -> "2131"
        self.assertEqual(self.calculator.sum("1234", "897"), "2131")

    def test_addition_with_carry(self):
        self.assertEqual(self.calculator.sum("999", "2"), "1001")

    def test_zero_addition(self):
        self.assertEqual(self.calculator.sum("0", "0"), "0")

    def test_different_lengths(self):
        self.assertEqual(self.calculator.sum("12345", "5"), "12350")

    def test_large_numbers(self):
        self.assertEqual(self.calculator.sum("999999999999999999", "1"), "1000000000000000000")

if __name__ == "__main__":
    unittest.main()