_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reveal-cards-in-increasing-order/
# In a deck of cards, every card has a unique integer. You can order the deck in any order you want.
# Initially, all the cards start face down (unrevealed) in one deck.
# Now, you do the following steps repeatedly, until all cards are revealed:
# Take the top card of the deck, reveal it, and take it out of the deck.
# If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
# If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.
# The first entry in the answer is considered to be the top of the deck.

# For each card from lowest to highest, add the card to the next empty index in the result.
# Then move to next empty index to the back of the queue of indices - the card that is ultimately placed here will
# be moved to the bottom of the deck.
# Time - O(n log n)
# Space - O(n)

from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        index = deque(range(n))
        result = [None] * n

        for card in sorted(deck):

            result[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return result