
import unittest
from lambda_app.Calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(divide(10, 5), 2)

    def test_division_with_decimal_result(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_division_by_zero(self):
        self.assertEqual(
            divide(10, 0),
            "Error: Division by zero is not allowed."
        )

    def test_addition_with_zero(self):
        self.assertEqual(add(10, 0), 10)

    def test_subtraction_negative_result(self):
        self.assertEqual(subtract(5, 10), -5)


if __name__ == "__main__":
    unittest.main()
