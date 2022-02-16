#!/usr/bin/env python3

import unittest

def number_of_consonants(s: str) -> int:
    """
    Takes a string 's' and returns the number of consonants in the string.
    Consonants will be defined as the 26 letters of the english alphabet minus the vowels 'a','e','i','o', and 'u'.
    'y' will count as a consonants for this exercise.
    Note: 's' may have both upercase, lowercase, and non-alphabet characters(numbers or symbols)

    eg. square_number("Hello World!!") == 7

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
class TestNumberOfConsonants(unittest.TestCase):
    def test_example(self):
        self.assertEqual(number_of_consonants("Hello World!!"), 7)

    def test_empty_string(self):
        self.assertEqual(number_of_consonants(""), 0)

    def test_all_consonants(self):
        self.assertEqual(number_of_consonants("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"), 42)

    def test_symbols(self):
        self.assertEqual(number_of_consonants("`!@#$%^&*()_+{}|:\"<>?,./;'[]\\1234567890-='"), 0)

    def test_uppercase_string(self):
        self.assertEqual(number_of_consonants("THE BEE, OF COURSE, FLIES ANYWAY"), 14)

    def test_lowercase_string(self):
        self.assertEqual(number_of_consonants("because bees don't care what humans think is impossible."), 28)

    def test_no_consonants(self):
        self.assertEqual(number_of_consonants("eo, a. eo, a. eo, a. eo, a. Oo, a a eo! ea, e' ae i u a ie."), 0)



if __name__=="__main__":
    unittest.main()
