#!/usr/bin/env python3

import unittest

def sum_of_odd_numbers(n: int) -> int:
    """
    Takes a positive integer 'n' and returns the sum of the odd numbers from 1 up to and including 'n'.
    Can assume that n >= 1

    eg. sum_of_odd_numbers(7) == 1+3+5+7 == 16

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

    def test_first_10(self):
        self.assertEqual(sum_of_odd_numbers(1), 1)
        self.assertEqual(sum_of_odd_numbers(2), 1)
        self.assertEqual(sum_of_odd_numbers(3), 4)
        self.assertEqual(sum_of_odd_numbers(4), 4)
        self.assertEqual(sum_of_odd_numbers(5), 9)
        self.assertEqual(sum_of_odd_numbers(6), 9)
        self.assertEqual(sum_of_odd_numbers(7), 16)
        self.assertEqual(sum_of_odd_numbers(8), 16)
        self.assertEqual(sum_of_odd_numbers(9), 25)
        self.assertEqual(sum_of_odd_numbers(10),25)

    def test_large(self):
        self.assertEqual(sum_of_odd_numbers(1000), 250000)

if __name__=="__main__":
    unittest.main()
