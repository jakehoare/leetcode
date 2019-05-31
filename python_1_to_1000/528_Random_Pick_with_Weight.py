_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/random-pick-with-weight/
# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which
# randomly picks an index in proportion to its weight.

# Create a list of cumulative weights. Choose a random integer between 1 and the sum of all weights. Binary search the
# cumulative list for the index where the random integer would be inserted and return that index. Probability of
# choosing an index is proprtional to its weight.
# Time - O(n log n) for number of weights n
# Space - O(n)

import random, bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cumulative = []
        total = 0
        for weight in w:
            total += weight
            self.cumulative.append(total)

    def pickIndex(self):
        """
        :rtype: int
        """
        x = random.randint(1, self.cumulative[-1])
        return bisect.bisect_left(self.cumulative, x)