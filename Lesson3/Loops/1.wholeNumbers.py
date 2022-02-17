#!/usr/bin/env python3

import unittest
from typing import List

def natural_nums(n: int) -> List[int]:
    """
    Takes a positive integer 'n' and returns a list of the first 'n' whole numbers.
    Can assume that n >= 0

    eg. natural_nums(7) == [0,1,2,3,4,5,6]

    Definition of natural numbers: https://byjus.com/maths/whole-numbers/
        eg. 0,1,2,3,4,5,6...
    Idealy, this function would be returning a generator/iterator and not a list but for ease of learning and testing, it will be a list.
    """

    output: List[int] = []

    #Your code here
    #Replacing 'print' with 'output.append' should work
    #Eg. output.append(i)

    return output



"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestNaturalNums(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(natural_nums(0), [])

    def test_first_10(self):
        self.assertEqual(natural_nums(1), [0])
        self.assertEqual(natural_nums(2), [0,1])
        self.assertEqual(natural_nums(3), [0,1,2])
        self.assertEqual(natural_nums(4), [0,1,2,3])
        self.assertEqual(natural_nums(5), [0,1,2,3,4])
        self.assertEqual(natural_nums(6), [0,1,2,3,4,5])
        self.assertEqual(natural_nums(7), [0,1,2,3,4,5,6])
        self.assertEqual(natural_nums(8), [0,1,2,3,4,5,6,7])
        self.assertEqual(natural_nums(9), [0,1,2,3,4,5,6,7,8])
        self.assertEqual(natural_nums(10),[0,1,2,3,4,5,6,7,8,9])

    def test_large(self):
        self.assertEqual(natural_nums(1000), list(range(1000)))

if __name__=="__main__":
    unittest.main()
