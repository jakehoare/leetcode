_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/power-of-four/
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# If log base 4 is not an integer then rounding to integer and raising to power 4 will not return the original num.
# Time - O(1)
# Space - O(1)

import math

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        return 4 ** int(math.log(num, 4)) == num

