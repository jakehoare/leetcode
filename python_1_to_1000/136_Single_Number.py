_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/single-number/
# Given an array of integers, every element appears twice except for one. Find that single one.

# Any number xor with itself is zero.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for num in nums:
            xor ^= num
        return xor