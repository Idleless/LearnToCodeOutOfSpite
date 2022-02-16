#!/usr/bin/env python3

import unittest

def sum_of_even_numbers(n: int) -> int:
    """
    Takes a positive integer 'n' and returns the sum of the even numbers from 0 up to and including 'n'.
    Can assume that n >= 0

    eg. sum_of_even_numbers(7) == 0+2+4+6 == 12

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
        self.assertEqual(sum_of_even_numbers(0), 0)

    def test_first_10(self):
        self.assertEqual(sum_of_even_numbers(1), 0)
        self.assertEqual(sum_of_even_numbers(2), 2)
        self.assertEqual(sum_of_even_numbers(3), 2)
        self.assertEqual(sum_of_even_numbers(4), 6)
        self.assertEqual(sum_of_even_numbers(5), 6)
        self.assertEqual(sum_of_even_numbers(6), 12)
        self.assertEqual(sum_of_even_numbers(7), 12)
        self.assertEqual(sum_of_even_numbers(8), 20)
        self.assertEqual(sum_of_even_numbers(9), 20)
        self.assertEqual(sum_of_even_numbers(10),30)

    def test_large(self):
        self.assertEqual(sum_of_even_numbers(1000), 250500)

if __name__=="__main__":
    unittest.main()
