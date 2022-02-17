#!/usr/bin/env python3

import unittest
from typing import List

def printing_numbers(n: int) -> List[str]:
    """
    Takes a positive integer 'n' and returns a list of strings with the following pattern:
        The first index will be a string with the numbers 'n' to 1
        The second index will be a string with the numbers 'n'-1 to 1
        The third index will be a string with the numbers 'n'-2 to 1
        ...
        The last index will be the number 1
    Can assume that n >= 1

    eg. printing_numbers(5) == [
        "54321",
        "4321",
        "321",
        "21",
        "1"
    ]

    """

    output: List[str] = []

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
class TestPrintingNumbers(unittest.TestCase):
    def test_example(self):
        self.assertEqual(printing_numbers(5), ["54321","4321","321","21","1"])

    def test_fist_7(self):
        self.assertEqual(printing_numbers(1), ["1"])
        self.assertEqual(printing_numbers(2), ["21","1"])
        self.assertEqual(printing_numbers(3), ["321","21","1"])
        self.assertEqual(printing_numbers(4), ["4321","321","21","1"])
        self.assertEqual(printing_numbers(5), ["54321","4321","321","21","1"])
        self.assertEqual(printing_numbers(6), ["654321","54321","4321","321","21","1"])
        self.assertEqual(printing_numbers(7), ["7654321","654321","54321","4321","321","21","1"])
        self.assertEqual(printing_numbers(8), ["87654321","7654321","654321","54321","4321","321","21","1"])
        self.assertEqual(printing_numbers(9), ["987654321","87654321","7654321","654321","54321","4321","321","21","1"])
        self.assertEqual(printing_numbers(10), ["10987654321","987654321","87654321","7654321","654321","54321","4321","321","21","1"])

if __name__=="__main__":
    unittest.main()
