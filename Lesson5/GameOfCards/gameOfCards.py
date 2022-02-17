#!/usr/bin/env python3

import unittest
from typing import List

def game_of_cards(n: int) -> List[tuple[int, str]]:
    """
    Takes an integer 'n' and returns random hand of 'n' cards from a 52 card deck.
    A hand will be a list of cards.
    A card will be a tuple of an integer for the value of the card and a string for the suit of the card.
        ie. The 7 of Spades will be (7,"Spade")
    Face cards will be the numbers 11 to 13.
        Jack = 11
        Queen = 12
        King = 13
    Ace will be the value 1
    The four suits will be "Heart", "Diamond", "Spade", and "Club"
    Assume 0 <= n <= 52
    Note: All cards returned must be unique.
    Recommended libraries: random.shuffle, itertools.product

    eg. game_of_cards(6) == [(7,"Spade"), (12, "Diamond"), (9, "Heart"), (10, "Heart"), (11, "Spade"), (5, "Club")]
        Of course, your cards will be diffrent as the hands must be random.
    """

    output: List[tuple[int,str]] = []

    #Your code here

    return output


"""
##########################################################################
                    Testing Interface below
     Can ignore or used as a refrence but shouldn't need to change
##########################################################################
"""
class TestGameOfCards(unittest.TestCase):
    SUITS = ["Heart", "Diamond", "Spade", "Club"]

    # Helper function to check if the cards in the hand are valid
    def check_cards(self, cards: List[tuple[int,str]], expected_num_of_cards: int):

        # check that the right number of cards is returned
        self.assertEqual(len(cards), expected_num_of_cards)

        for card in cards:
            # check that the card has a valid value
            self.assertTrue(1<=card[0]<=13)
            # check that the correct suit was used
            self.assertIn(card[1], self.SUITS)

        # check that all cards are unique
        # Note: the set function is being used to removed duplicats.
        #   As all the cards should be unique, no cards should be removed and the length unchanged.
        self.assertEqual(len(set(cards)), len(cards))

    def test_example(self):
        cards = game_of_cards(5)
        self.check_cards(cards, 5)


    def test_zero_cards(self):
        self.assertEqual(game_of_cards(0), [])

    def test_whole_deck(self):
        cards = game_of_cards(52)
        self.check_cards(cards, 52)


    def test_uniq_hands(self):
        cards_a = game_of_cards(10)
        cards_b = game_of_cards(10)

        # There is a 1 in 57,407,703,889,536,000 chance that this will be a false positive.
        # Or there is an issue with your randomization.
        self.assertNotEqual(cards_a, cards_b)


if __name__=="__main__":
    unittest.main()
