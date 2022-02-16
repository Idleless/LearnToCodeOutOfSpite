#!/usr/bin/env python3

import unittest

def reverse_string(s: str) -> str:
    """
    Takes a string 's' and returns the reverse of string 's'.
    Note: 's' may be an empty string ("")

    eg. reverse_string("HelloWorld") == "dlroWolleH"

    """

    output = ""

    #Your code here
    
    return output


"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestReverseString(unittest.TestCase):
    def test_example(self):
        self.assertEqual(reverse_string("HelloWorld"), "dlroWolleH")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_rev_rev(self):
        self.assertEqual(reverse_string(reverse_string("Never gonna give you up")), "Never gonna give you up")

    def test_unRev(self):
        self.assertEqual(reverse_string("nwod uoy tel annog reveN"), "Never gonna let you down")

    def test_spoon(self):
        self.assertEqual(reverse_string("spoonfeed"), "deefnoops")

if __name__=="__main__":
    unittest.main()
