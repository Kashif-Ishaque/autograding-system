import unittest
from solution import calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate(10, 5, "add"), 15)

    def test_subtract(self):
        self.assertEqual(calculate(10, 5, "subtract"), 5)

    def test_multiply(self):
        self.assertEqual(calculate(10, 5, "multiply"), 50)

    def test_divide(self):
        self.assertEqual(calculate(10, 5, "divide"), 2.0)
        self.assertEqual(calculate(10, 0, "divide"), "Cannot divide by zero")

    def test_invalid_operation(self):
        self.assertEqual(calculate(10, 5, "modulus"), "Invalid operation")

if __name__ == "__main__":
    unittest.main()
