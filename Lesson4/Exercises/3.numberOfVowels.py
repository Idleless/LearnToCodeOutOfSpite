#!/usr/bin/env python3

import unittest

def number_of_vowels(s: str) -> int:
    """
    Takes a string 's' and returns the number of vowels in the string.
    Vowels will be defined as  'a','e','i','o', and 'u'. 'y' will not count as a vowel for this exercise.
    Note: 's' may have both upercase, lowercase, and non-alphabet characters(numbers or symbols)

    eg. square_number("Hello World!!") == 3

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
class TestNumberOfVowels(unittest.TestCase):
    def test_example(self):
        self.assertEqual(number_of_vowels("Hello World!!"), 3)

    def test_empty_string(self):
        self.assertEqual(number_of_vowels(""), 0)

    def test_all_vowels(self):
        self.assertEqual(number_of_vowels("AEIOUaeiouAeIoU"), 15)

    def test_symbols(self):
        self.assertEqual(number_of_vowels("`!@#$%^&*()_+{}|:\"<>?,./;'[]\\1234567890-='"), 0)

    def test_uppercase_string(self):
        self.assertEqual(number_of_vowels("ACCORDING TO ALL KNOWN LAWS OF AVIATION,"), 13)

    def test_lowercase_string(self):
        self.assertEqual(number_of_vowels("there is no way that a bee should be able to fly."), 15)

    def test_no_vowels(self):
        self.assertEqual(number_of_vowels("1ts w1ngs 4r3 t00 sm4ll t0 g3t 1ts f4t l1ttl3 b0dy 0ff th3 gr0vnd"), 0)



if __name__=="__main__":
    unittest.main()
