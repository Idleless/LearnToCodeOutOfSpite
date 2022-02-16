#!/usr/bin/env python3

import unittest

def square_number(n: int) -> int:
    """
    Takes an integer 'n' and returns the value of 'n' squared.
    Note: 'n' can be positive or negative (or zero)
    eg. square_number(7) == 49

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
class TestSquareNumber(unittest.TestCase):
    def test_example(self):
        self.assertEqual(square_number(7), 49)

    def test_zero(self):
        self.assertEqual(square_number(0), 0)

    def test_positive(self):
        self.assertEqual(square_number(1), 1)
        self.assertEqual(square_number(2), 4)
        self.assertEqual(square_number(3), 9)
        self.assertEqual(square_number(4), 16)
        self.assertEqual(square_number(10), 100)

    def test_negative(self):
        self.assertEqual(square_number(-1), 1)
        self.assertEqual(square_number(-2), 4)
        self.assertEqual(square_number(-3), 9)
        self.assertEqual(square_number(-4), 16)
        self.assertEqual(square_number(-10), 100)

if __name__=="__main__":
    unittest.main()
