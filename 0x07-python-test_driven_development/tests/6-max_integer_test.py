"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """test max integer class"""

    def test_empty_list(self):
        """test empty list"""

        result = max_integer([])
        self.assertEqual(result, None)

    def test_default_argument(self):
        """test default argument"""

        result = max_integer()
        self.assertEqual(result, None)

    def test_postivie_numbers(self):
        """test postivie numbers"""

        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        """test negative numbers"""

        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_one_element(self):
        """test one element"""

        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_max_in_middle(self):
        """test max in the middle"""

        result = max_integer([0, 3, 2])
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
