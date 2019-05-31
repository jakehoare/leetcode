_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# In a deck of cards, each card has an integer written on it.
# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into
# 1 or more groups of cards, where:
# Each group has exactly X cards.
# All the cards in each group have the same integer.

# Count the number of each card. Attempt all values of X from 2 to the size of the smallest group. Check whether
# each group is divisible by X.
# Time - O(n**2)
# Space - O(n)

from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        freq = Counter(deck)

        min_count = min(freq.values())
        if min_count == 1:              # each group must have at least 2 cards
            return False

        for X in range(2, min_count + 1):
            if all(count % X == 0 for count in freq.values()):
                return True

        return False