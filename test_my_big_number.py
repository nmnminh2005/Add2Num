import unittest
from my_big_number import MyBigNumber


class TestMyBigNumber(unittest.TestCase):

    def setUp(self):
        self.calculator = MyBigNumber()

    def test_normal_addition(self):
        self.assertEqual(
            self.calculator.sum("1235", "897"),
            "2132"
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
            self.calculator.sum(
                "999999999999999999",
                "1"
            ),
            "1000000000000000000"
        )


if __name__ == "__main__":
    unittest.main()