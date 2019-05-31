_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements
# equal, where a move is incrementing n - 1 elements by 1.

# Incrementing n - 1 elements is equivalent to incrementing all n elements and decrementing 1 element. Incrementing all
# elements does not equalize the array, so we need to count the number of moves to decrement all elements to be equal.
# For each element, this is the difference between its value and the minimum value.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)