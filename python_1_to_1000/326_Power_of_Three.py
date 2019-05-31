_author_ = 'jake'
_project_ = 'leetcode'


# https://leetcode.com/problems/power-of-three/
# Given an integer, write a function to determine if it is a power of three.

# Find the maximum power of 3 within a 4 byte signed integer. When divided by a power of 3, this number will have no
# remainder.
# Time - O(1)
# Space - O(1)

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        max_int = 2 ** 31 - 1
        max_power = int(math.log(max_int, 3))
        return 3 ** max_power % n == 0
