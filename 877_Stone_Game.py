_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/stone-game/
# Alex and Lee play a game with piles of stones.
# There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones. The total number of stones is odd, so there are no ties.
# Alex and Lee take turns, with Alex starting first.
# Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

# Alex can initially take the first pile (an even index) or the last pile (an odd index). If Alex takes an even index
# pile then Lee must take an odd index pile, and Alex can take an even index pile next. If Alex take an odd index pile
# initially, Lee must take an even index pile and Alex can take an odd index pile next.
# Thus Alex can take all even or all odd index piles. Since the sum of even piles and odd piles are not equal
# (because the total sum is odd), Alex can always take more stones in total.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True