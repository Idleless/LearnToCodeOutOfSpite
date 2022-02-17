#!/usr/bin/env python3

import unittest
from typing import List

def printing_numbers(n: int) -> List[str]:
    """
    Takes a positive integer 'n' and returns a list of strings with the following pattern:
        The first index will be a string with 'n' '*'
        The second index will be a string with 'n'-1 '*'
        The third index will be a string with 'n'-2 '*'
        ...
        The last index will be the number 1
    Can assume that n >= 1

    eg. printing_numbers(5) == [
        "*****",
        "****",
        "***",
        "**",
        "*"
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
        self.assertEqual(printing_numbers(5), ["*****","****","***","**","*"])

    def test_fist_7(self):
        self.assertEqual(printing_numbers(1), ["*"])
        self.assertEqual(printing_numbers(2), ["**","*"])
        self.assertEqual(printing_numbers(3), ["***","**","*"])
        self.assertEqual(printing_numbers(4), ["****","***","**","*"])
        self.assertEqual(printing_numbers(5), ["*****","****","***","**","*"])
        self.assertEqual(printing_numbers(6), ["******","*****","****","***","**","*"])
        self.assertEqual(printing_numbers(7), ["*******","******","*****","****","***","**","*"])
        self.assertEqual(printing_numbers(8), ["********","*******","******","*****","****","***","**","*"])
        self.assertEqual(printing_numbers(9), ["*********","********","*******","******","*****","****","***","**","*"])
        self.assertEqual(printing_numbers(10), ["**********","*********","********","*******","******","*****","****","***","**","*"])

if __name__=="__main__":
    unittest.main()
