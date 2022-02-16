#!/usr/bin/env python3

import unittest

def minimum(a: int, b: int, c: int) -> int:
    """
    Takes three integer 'a','b', and 'c' and returns the smallest of them (closest to -inf).
    Note: Any of the integers can be negative

    eg. minimum(4,2,0) == 0

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
class TestMinimum(unittest.TestCase):
    def test_example(self):
        self.assertEqual(minimum(4,2,0), 0)

    def test_min_in_diff_locations(self):
        self.assertEqual(minimum(1,2,3), 1)
        self.assertEqual(minimum(2,1,3), 1)
        self.assertEqual(minimum(2,3,1), 1)

    def test_all_equal(self):
        self.assertEqual(minimum(1,1,1), 1)

    def test_all_zero(self):
        self.assertEqual(minimum(0,0,0),0)

    def test_all_negative(self):
        self.assertEqual(minimum(-1,-2,-3),-3)

    def test_mixed(self):
        self.assertEqual(minimum(-1,0,1), -1)

if __name__=="__main__":
    unittest.main()
