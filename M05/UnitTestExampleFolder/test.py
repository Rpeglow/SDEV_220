"""
Reed Peglow
SDEV 220
M05 Programming Assignment - Testing
"""

import unittest
#Imports sum() from the my_sum package
from my_sum import sum
from fractions import Fraction

#a new test case class called TestSum, 
# which inherits from unittest.TestCase
class TestSum(unittest.TestCase):
    
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

# a command-line entry point, which runs the unittest test-runner .main()
if __name__ == '__main__':
    unittest.main()

"""What do the test results mean?
The results will tell you if you have made errors in sections of your code,
 It will also tell if tests are passed or failed and where the error is occuring.
 They also give you the speed at which the test ran in case optimization is a goal"""