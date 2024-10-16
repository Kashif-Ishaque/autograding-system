import unittest
from solution import fibonacci  # Make sure the student submits the function in solution.py

class TestFibonacci(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    def test_zero(self):
        self.assertEqual(fibonacci(0), [])

    def test_negative(self):
        self.assertEqual(fibonacci(-3), [])

if __name__ == '__main__':
    unittest.main()
