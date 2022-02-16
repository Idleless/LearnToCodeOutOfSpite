#!/usr/bin/env python3

import unittest

def subset_of_primes(start,end):
    """
    Takes two integers, 'start' and 'end', and returns a list of primes between 'start' and 'end' inclusive.
    Assume 0 <= start < end

    eg. subset_of_primes(5,13) == [5,7,11,13]

    Definition of prime numbers: https://byjus.com/maths/prime-numbers/
        eg. 2,3,5,7,11,13,17...
    """

    output = []

    #Your code here
    #Replacing 'print' with 'output.append' should work
    #Eg. output.append(i)

    return output



"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestNaturalNums(unittest.TestCase):
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    def test_example(self):
        self.assertEqual(subset_of_primes(5,13), [5,7,11,13])

    def test_no_primes(self):
        self.assertEqual(subset_of_primes(0,1), [])

    def test_first_1000(self):
        self.assertEqual(subset_of_primes(0,1000), self.PRIMES)

    def test_rand_ranges(self):
        self.assertEqual(subset_of_primes(10,30), self.PRIMES[self.PRIMES.index(11):self.PRIMES.index(29)+1])
        self.assertEqual(subset_of_primes(7,31), self.PRIMES[self.PRIMES.index(7):self.PRIMES.index(31)+1])
        self.assertEqual(subset_of_primes(14,106), self.PRIMES[self.PRIMES.index(17):self.PRIMES.index(103)+1])

if __name__=="__main__":
    unittest.main()
