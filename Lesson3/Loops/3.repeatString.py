#!/usr/bin/env python3

import unittest

def repeat_string(word: str, n: int) -> str:
    """
    Takes a string 'word' and an integer 'n' and returns a string with 'word' repeated 'n' times.
    Can assume that n >= 0

    eg. repeat_string("HelloWorld", 3) == "HelloWorldHelloWorldHelloWorld"
    """

    output = ""

    #Your code here
    #Note: to append to the end of the string, you can use '+='
    #    eg. output += "HelloWorld"

    return output


"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestSumOfNaturalNums(unittest.TestCase):
    def test_example(self):
        self.assertEqual(repeat_string("HelloWorld", 3), "HelloWorldHelloWorldHelloWorld")

    def test_empty_word(self):
        self.assertEqual(repeat_string("", 3), "")

    def test_empty_n(self):
        self.assertEqual(repeat_string("HelloWorld", 0), "")

    def test_roflcopter(self):
        self.assertEqual("My ROFLCopter goes" + repeat_string(" soi", 5), "My ROFLCopter goes soi soi soi soi soi")

if __name__=="__main__":
    unittest.main()
