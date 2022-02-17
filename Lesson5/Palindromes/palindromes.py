#!/usr/bin/env python3

import unittest

def is_palindrome(s: str) -> bool:
    """
    Takes a string 's' and returns True if the string is a palindrom, else it returns False.
    A palindrome is defined as a string that reads the same backwards or forwards.

    Note: Only alphanumeric characters will be checked; Spaces and special characters will be ignored.
        eg. is_palindrome("race car!!") == "!!rac ecar" => True
    Note: Alphabet cases (uppercase and lowercase) will be ignored (not case sensitive).
        eg. is_palindrome("Race Car") == "raC ecaR" => True

    """

    output = False

    #Your code here

    return output


"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestPalindrome(unittest.TestCase):
    def test_example(self):
        self.assertEqual(is_palindrome("racecar"), True)
        self.assertEqual(is_palindrome("race car"), True)
        self.assertEqual(is_palindrome("RaceCar"), True)
        self.assertEqual(is_palindrome("Race Car"), True)
        self.assertEqual(is_palindrome("Race Car!!"), True)

    def test_empty_string(self):
        self.assertEqual(is_palindrome(""), True)

    def test_not_palindrome(self):
        self.assertEqual(is_palindrome("Hello World"), False)
        self.assertEqual(is_palindrome("Error 418: I'm a teapot"), False)
        self.assertEqual(is_palindrome("Keyboard not responding. Press anykey to continue."), False)
        self.assertEqual(is_palindrome("An Error occurred while trying to display an error."), False)
        self.assertEqual(is_palindrome("Please wake up"), False)

    def test_numbers(self):
        self.assertEqual(is_palindrome("1331"), True)
        self.assertEqual(is_palindrome("13331"), True)
        self.assertEqual(is_palindrome("1234"), False)

    def test_complex(self):
        self.assertEqual(is_palindrome("Madam, I'm Adam."), True)
        self.assertEqual(is_palindrome("A man, a plan, a canal--Panama!"), True)
        self.assertEqual(is_palindrome("Do geese see God?"), True)
        self.assertEqual(is_palindrome("Murder for a jar of red rum."), True)
        self.assertEqual(is_palindrome("Go Hang a Salami! I'm a Lasagna Hog!"), True)

if __name__=="__main__":
    unittest.main()
