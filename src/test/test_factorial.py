'''
Created on 03-Jul-2024

@author: subhashis
'''

import unittest
import sys
import os

# Add the main directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from main.factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):

    def test_factorial_iterative(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(10), 3628800)

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(10), 3628800)

if __name__ == '__main__':
    unittest.main()

