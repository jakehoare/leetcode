_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/single-number-iii/
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements
# appear exactly twice. Find the two elements that appear only once.

# Xor all the numbers to create the xor of the 2 singles.  If a bit is set in this xor, it is set in one of the
# singles and not the other.  Find the first bit that is set, then find the xor of all nums with that bit set
# and the xor of all nums without that bit set.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor = xor ^ num

        bit = 0
        while not (1 << bit) & xor:
            bit += 1

        bit_set_xor, bit_not_set_xor = 0, 0
        for num in nums:
            if (1 << bit) & num:
                bit_set_xor = bit_set_xor ^ num
            else:
                bit_not_set_xor = bit_not_set_xor ^ num

        return [bit_set_xor, bit_not_set_xor]