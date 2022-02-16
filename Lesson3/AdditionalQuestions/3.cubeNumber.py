#!/usr/bin/env python3

import unittest

def cube_number(n: int) -> int:
    """
    Takes an integer 'n' and returns the value of 'n' cubed.
    Note: 'n' can be positive or negative (or zero)
    eg. cube_number(7) == 343

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
class TestCubeNumber(unittest.TestCase):
    def test_example(self):
        self.assertEqual(cube_number(7), 343)

    def test_zero(self):
        self.assertEqual(cube_number(0), 0)

    def test_positive(self):
        self.assertEqual(cube_number(1), 1)
        self.assertEqual(cube_number(2), 8)
        self.assertEqual(cube_number(3), 27)
        self.assertEqual(cube_number(4), 64)
        self.assertEqual(cube_number(10), 1000)

    def test_negative(self):
        self.assertEqual(cube_number(-1), -1)
        self.assertEqual(cube_number(-2), -8)
        self.assertEqual(cube_number(-3), -27)
        self.assertEqual(cube_number(-4), -64)
        self.assertEqual(cube_number(-10), -1000)

if __name__=="__main__":
    unittest.main()
