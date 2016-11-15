_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/single-number-ii/
# Given an array of integers, every element appears three times except for one. Find that single one.

# If a bit is set in num, but not set in ones or twos then that bit is then set in ones.
# If a bit is set in num, set in ones but not in twos then that bit is then set in twos and not ones.
# If a bit is set in num, but not set in ones or twos then that bit is then set in ones.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0

        for num in nums:
            ones = (ones ^ num) & ~twos     # xor of all nums that have appeared once only
            twos = (twos ^ num) & ~ones     # xor of all nums that have appeared twice only

        return ones
