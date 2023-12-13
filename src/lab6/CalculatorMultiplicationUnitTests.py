import random
import string
import unittest
from src.lab2.calculator import Calculator


class CalculatorMultiplicationUnitTests(unittest.TestCase):
    def test_multiply_positive_numbers_returns_correct_value(self):
        # Arrange
        test_num1 = random.randrange(1, 100) * 1.0
        test_num2 = random.randrange(1, 100) * 1.0
        operator = "*"
        expected = test_num1 * test_num2
        calc = Calculator(test_num1, test_num2, operator)

        # Act
        calc.calculate()
        result = calc.result

        # Assert
        self.assertEqual(expected, result)

    def test_multiply_positive_number_and_zero_returns_correct_value(self):
        # Arrange
        test_num1 = random.randrange(1, 100) * 1.0
        test_num2 = 0.0
        operator = "*"
        expected = test_num1 * test_num2
        calc = Calculator(test_num1, test_num2, operator)

        # Act
        calc.calculate()
        result = calc.result

        # Assert
        self.assertEqual(expected, result)

    def test_multiply_negative_numbers_returns_correct_value(self):
        # Arrange
        test_num1 = random.randrange(1, 100) * (-1.0)
        test_num2 = random.randrange(1, 100) * (-1.0)
        operator = "*"
        expected = test_num1 * test_num2
        calc = Calculator(test_num1, test_num2, operator)

        # Act
        calc.calculate()
        result = calc.result

        # Assert
        self.assertEqual(expected, result)

    def test_multiply_not_numbers_returns_error_value(self):
        # Arrange
        letters = string.ascii_letters
        test_num1 = ''.join(random.choice(letters) for i in range(10))
        test_num2 = ''.join(random.choice(letters) for i in range(10))
        operator = "*"

        calc = Calculator(test_num1, test_num2, operator)

        # Act
        with self.assertRaises(TypeError):
            result = calc.calculate()
