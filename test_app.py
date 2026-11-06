import unittest
from app import add_numbers

class TestApp(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_add_zero(self):
        self.assertEqual(add_numbers(5, 0), 5)

if __name__ == "__main__":
    unittest.main()
