import unittest
import math
import os
import sys
# import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import calculate_sqrt, calculate_factorial, calculate_ln, calculate_power

class TestCalculator(unittest.TestCase):


    def test_square_root(self):
  
        self.assertAlmostEqual(calculate_sqrt(16), 4.0)
        self.assertAlmostEqual(calculate_sqrt(0), 0.0)
        self.assertAlmostEqual(calculate_sqrt(2.25), 1.5)
        self.assertAlmostEqual(calculate_sqrt(2), 1.41421356, places=7)
        with self.assertRaises(ValueError):
            calculate_sqrt(-4)
        with self.assertRaises(TypeError):
            calculate_sqrt("four")

    def test_factorial(self):
        
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        with self.assertRaises(ValueError):
            calculate_factorial(-2)
        with self.assertRaises(TypeError):
            calculate_factorial(5.5)

    def test_natural_log(self):

        self.assertAlmostEqual(calculate_ln(math.e), 1.0)
        self.assertAlmostEqual(calculate_ln(1), 0.0)
        with self.assertRaises(ValueError):
            calculate_ln(0)
        with self.assertRaises(ValueError):
            calculate_ln(-5)
        with self.assertRaises(TypeError):
            calculate_ln("e")

    def test_power_function(self):
       
        self.assertEqual(calculate_power(2, 3), 8.0)
        self.assertEqual(calculate_power(5, 0), 1.0)
        self.assertEqual(calculate_power(0, 5), 0.0)
        self.assertEqual(calculate_power(0, 0), 1.0) 
        self.assertEqual(calculate_power(-2, 3), -8.0)
        self.assertEqual(calculate_power(-2, 2), 4.0)
        self.assertAlmostEqual(calculate_power(4, 0.5), 2.0)
        self.assertAlmostEqual(calculate_power(2, -2), 0.25)
        with self.assertRaises(ValueError):
            calculate_power(-4, 0.5)
        with self.assertRaises(TypeError):
            calculate_power("two", 3)

if __name__ == "__main__":
    unittest.main()
