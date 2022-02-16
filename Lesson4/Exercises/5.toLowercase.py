#!/usr/bin/env python3

import unittest

def to_lowercase(s: str) -> str:
    """
    Takes a string 's' and returns the same string with any upercase letters changed to lowercase.
    Note: 's' may have both upercase, lowercase, and non-alphabet characters(numbers or symbols)

    eg. to_lowercase("Hello World!!") == "hello world!!"

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
class TestToLowercase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(to_lowercase("Hello World!!"), "hello world!!")

    def test_empty_string(self):
        self.assertEqual(to_lowercase(""), "")

    def test_symbols(self):
        self.assertEqual(to_lowercase("`!@#$%^&*()_+{}|:\"<>?,./;'[]\\1234567890-='"), "`!@#$%^&*()_+{}|:\"<>?,./;'[]\\1234567890-='")

    def test_all_uppercase(self):
        self.assertEqual(to_lowercase("BARRY! BREAKFAST IS READY!"), "barry! breakfast is ready!")

    def test_all_lowercase(self):
        self.assertEqual(to_lowercase("coming! oh, hang on a second. hello?"), "coming! oh, hang on a second. hello?")

if __name__=="__main__":
    unittest.main()
