import unittest
import math
from calculator import square_root, factorial, natural_log, power_function


def sqrt_test(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def factorial_test(x):
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(x)

def ln_test(x):
    if x <= 0:
        raise ValueError("Natural log only defined for positive numbers")
    return math.log(x)

def power_test(x, b):
    return math.pow(x, b)

# Unit Tests 
class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(sqrt_test(16), 4)
        self.assertAlmostEqual(sqrt_test(0), 0)
        with self.assertRaises(ValueError):
            sqrt_test(-4)

    def test_factorial(self):
        self.assertEqual(factorial_test(5), 120)
        self.assertEqual(factorial_test(0), 1)
        with self.assertRaises(ValueError):
            factorial_test(-2)

    def test_natural_log(self):
        self.assertAlmostEqual(ln_test(math.e), 1)
        with self.assertRaises(ValueError):
            ln_test(0)
        with self.assertRaises(ValueError):
            ln_test(-5)

    def test_power_function(self):
        self.assertEqual(power_test(2, 3), 8)
        self.assertEqual(power_test(5, 0), 1)
        self.assertEqual(power_test(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
