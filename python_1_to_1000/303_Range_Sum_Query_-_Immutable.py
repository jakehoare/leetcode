_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-sum-query-immutable/
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Store cumulative sums.
# Time - O(n) for __init__(), O(1) for sumRange()
# Space - O(n)

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumul = [0]
        for num in nums:
            self.cumul.append(self.cumul[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumul[j + 1] - self.cumul[i]