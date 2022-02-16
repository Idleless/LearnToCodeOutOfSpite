#!/usr/bin/env python3

import unittest

def number_of_digits(n: int) -> int:
    """
    Takes an integer 'n' and returns the number of digits in the number 'n'.
    Note: 'n' may be negative.

    eg. number_of_digits(90210) == 5
    eg. number_of_digits(-1337) == 4

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
class TestNumberOfDigits(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(number_of_digits(90210), 5)
    def test_example2(self):
        self.assertEqual(number_of_digits(-1337), 4)

    def test_zero(self):
        self.assertEqual(number_of_digits(0),1)

    def test_positive(self):
        self.assertEqual(number_of_digits(1),1)
        self.assertEqual(number_of_digits(9),1)
        self.assertEqual(number_of_digits(10),2)
        self.assertEqual(number_of_digits(50),2)
        self.assertEqual(number_of_digits(99),2)
        self.assertEqual(number_of_digits(100),3)
        self.assertEqual(number_of_digits(500),3)
        self.assertEqual(number_of_digits(999),3)
        self.assertEqual(number_of_digits(1000),4)

    def test_negative(self):
        self.assertEqual(number_of_digits(-1),1)
        self.assertEqual(number_of_digits(-9),1)
        self.assertEqual(number_of_digits(-10),2)
        self.assertEqual(number_of_digits(-50),2)
        self.assertEqual(number_of_digits(-99),2)
        self.assertEqual(number_of_digits(-100),3)
        self.assertEqual(number_of_digits(-500),3)
        self.assertEqual(number_of_digits(-999),3)
        self.assertEqual(number_of_digits(-1000),4)

    def test_large(self):
        self.assertEqual(number_of_digits(100000000000),12)
        self.assertEqual(number_of_digits(-100000000000),12)
        self.assertEqual(number_of_digits(999999999999),12)
        self.assertEqual(number_of_digits(-999999999999),12)
        self.assertEqual(number_of_digits(10000000000000000000),20)
        self.assertEqual(number_of_digits(-10000000000000000000),20)
        self.assertEqual(number_of_digits(99999999999999999999),20)
        self.assertEqual(number_of_digits(-99999999999999999999),20)

if __name__=="__main__":
    unittest.main()
