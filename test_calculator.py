import unittest
from calculator import add
from calculator import sub

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(2, 3), -1)
        self.assertEqual(sub(10, 1), 9)

if __name__ == "__main__":
    unittest.main()
