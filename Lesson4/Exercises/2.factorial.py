#!/usr/bin/env python3

import unittest

def factorial(n: int) -> int:
    """
    Takes an integer 'n' and returns the value of 'n'! (factorial).
    Assume 'n' >= 0

    eg. factorial(7) == 7*6*5*4*3*2*1 == 5040

    Definition of factorial: https://byjus.com/maths/factorial/
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

class TestFactorial(unittest.TestCase):
    def test_example(self):
        self.assertEqual(factorial(7), 5040)

    def test_zero(self):
        # This is definitely an odd edge case but factorial(0) does equal 1
        self.assertEqual(factorial(0), 1)

    def test_first_five(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

    def test_ten(self):
        self.assertEqual(factorial(10), 3628800)

if __name__=="__main__":
    unittest.main()
