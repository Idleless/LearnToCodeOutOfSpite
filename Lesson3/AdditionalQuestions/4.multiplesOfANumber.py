#!/usr/bin/env python3

import unittest


def multiples_of_a_number(factor: int, num: int) -> [int]:
    """
    Takes an integer 'factor' and an integer 'num' and returns a list of the first 'num' multiples of 'factor' starting at 0.
    Assume num >= 1
    Note: factor may be negative

    eg. multiples_of_a_number(3,5) == [0*3, 1*3, 2*3, 3*3, 4*3] == [0,3,6,9,12]
    """

    output = []

    #Your code here

    return output


"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestMultiplesOfANumber(unittest.TestCase):
    def test_example(self):
        self.assertEqual(multiples_of_a_number(3,5), [0,3,6,9,12])

    def test_zero_factor(self):
        self.assertEqual(multiples_of_a_number(0,5), [0,0,0,0,0])

    def test_one_num(self):
        self.assertEqual(multiples_of_a_number(5,1), [0])

    def test_six_times_table(self):
        self.assertEqual(multiples_of_a_number(6,11),[0,6,12,18,24,30,36,42,48,54,60])



if __name__=="__main__":
    unittest.main()
