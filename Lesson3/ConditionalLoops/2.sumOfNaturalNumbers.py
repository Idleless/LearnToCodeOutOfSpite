#!/usr/bin/env python3

import unittest

def sum_of_natural_numbers(n: int) -> int:
    """
    Takes a positive integer 'n' and returns the sum of the first 'n' natural numbers.
    Can assume that n >= 0

    eg. sum_of_natural_numbers(7) == 28

    Definition of natural numbers: https://byjus.com/maths/natural-numbers/
        eg. 1,2,3,4,5,6...
    """

    output = 0

    #Your code here


    return output



"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestSumOfNaturalNums(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(sum_of_natural_numbers(0), 0)

    def test_first_10(self):
        self.assertEqual(sum_of_natural_numbers(1), 1)
        self.assertEqual(sum_of_natural_numbers(2), 3)
        self.assertEqual(sum_of_natural_numbers(3), 6)
        self.assertEqual(sum_of_natural_numbers(4), 10)
        self.assertEqual(sum_of_natural_numbers(5), 15)
        self.assertEqual(sum_of_natural_numbers(6), 21)
        self.assertEqual(sum_of_natural_numbers(7), 28)
        self.assertEqual(sum_of_natural_numbers(8), 36)
        self.assertEqual(sum_of_natural_numbers(9), 45)
        self.assertEqual(sum_of_natural_numbers(10),55)

    def test_large(self):
        self.assertEqual(sum_of_natural_numbers(1000), 500500)

if __name__=="__main__":
    unittest.main()
