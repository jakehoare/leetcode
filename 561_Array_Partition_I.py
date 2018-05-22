_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/array-partition-i/
# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2),
# ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Sort nums. The smallest num must be paired with some other num that will not form part of the sum. In order to
# maximise the sum, the smallest number should be paired with the next smallest. Pair each number with the next larger
# number, hence numbers of even indices form the resulting sum.
# Time - O(n log n)
# Space - O(n) for the sorted list

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])   # iterate with step of 2 to select even indices