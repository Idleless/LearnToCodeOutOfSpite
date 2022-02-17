#!/usr/bin/env python3

import unittest
import hashlib

def product_of_pythagorean_triplets(n: int) -> int | bool :
    """
    Takes an integer 'n' which is the sum of a triplet and returns the product of the triplet
        if a valid pythagorean triplet exists, else it returns False.
    Assume n >=3
    A pythagorean is defined as a set of three positive (non-zero) integers 'a', 'b', and 'c'
        such that 'a'**2 + 'b'**2 == 'c'**2
        https://byjus.com/maths/pythagorean-triples/

    eg. product_of_pythagorean_triplets(12):
            3 + 4 + 5 == 12,
            (3**2 + 4**2 == 5**2) == (9 + 16 == 25) == (True),
            => 3*4*5 == 60,
            returns 60

    eg. product_of_pythagorean_triplets(13):
            There does not exists a pathagorean triplet such that 'a' + 'b' + 'c' == 13
            Therefore: returns False
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
class TestPathagoreanTriplets(unittest.TestCase):
    def test_example_true(self):
        self.assertEqual(product_of_pythagorean_triplets(3+4+5), 3*4*5) #12 => 60

    def test_example_false(self):
        self.assertEqual(product_of_pythagorean_triplets(13), False)

    def test_valid_triplets(self):
        self.assertEqual(product_of_pythagorean_triplets(154), 120120)
        self.assertEqual(product_of_pythagorean_triplets(23+264+265), 23*264*265)
        self.assertEqual(product_of_pythagorean_triplets(15+112+113), 15*112*113)
        self.assertEqual(product_of_pythagorean_triplets(16+63+65), 16*63*65)
        self.assertEqual(product_of_pythagorean_triplets(19+180+181), 19*180*181)

    def test_invalid_tripets(self):
        self.assertEqual(product_of_pythagorean_triplets(3), False)
        self.assertEqual(product_of_pythagorean_triplets(11), False)
        self.assertEqual(product_of_pythagorean_triplets(22), False)
        self.assertEqual(product_of_pythagorean_triplets(123), False)
        self.assertEqual(product_of_pythagorean_triplets(53), False)
        self.assertEqual(product_of_pythagorean_triplets(443), False)
        self.assertEqual(product_of_pythagorean_triplets(21), False)

    def test_final(self):
        product = product_of_pythagorean_triplets(1000)
        hash = hashlib.sha256(str(product).encode()).hexdigest()
        self.assertEqual(hash, "d912d9d473ef86f12da1fb2011c5c0c155bd3a0ebdb4bbd7ea275cecdcb63731")


if __name__=="__main__":
    unittest.main()
