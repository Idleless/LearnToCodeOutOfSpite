#!/usr/bin/env python3

import unittest

def sort_string(s: str) -> str:
    """
    Takes a string 's' and returns a sorted string 's' in ascii order.
    Assume 's' only contains upercase and lowercase letters (no numbers, spaces, nor symbols)
    Note: 's' may be an empty string ("")
    Note: Uppercase letters are before lowercase.

    eg. sort_string("HelloWorld") == "HWdellloor"

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
class TestsortString(unittest.TestCase):
    def test_example(self):
        self.assertEqual(sort_string("HelloWorld"), "HWdellloor")

    def test_empty_string(self):
        self.assertEqual(sort_string(""), "")

    def test_rev_rev(self):
        self.assertEqual(sort_string(sort_string("Nevergonnagiveyouup")), "Naeeegginnoopruuvvy")

    def test_spoon(self):
        self.assertEqual(sort_string("spoonfeed"), "deefnoops")

if __name__=="__main__":
    unittest.main()
