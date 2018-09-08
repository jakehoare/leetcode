_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reordered-power-of-2/
# Starting with a positive integer N, we reorder the digits in any order (including the original order)
# such that the leading digit is not zero.
# Return true if and only if we can do this in a way such that the resulting number is a power of 2.

# Find the smallest power of 2 with the same length as N. Check the digit of this and all subsequent powers of 2
# until the length is greater than N.
# Time - O(log n)
# Space - O(log n)

from math import ceil, log
from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digit_count = Counter(str(N))                               # count the digits of N
        len_N = len(str(N))
        power_of_two = 2 ** int(ceil(log(10 ** (len_N - 1), 2)))    # the smallest power of 2 of length len_N
        str_power_of_two = str(power_of_two)

        while len(str_power_of_two) == len_N:                       # until length is too long
            if Counter(str_power_of_two) == digit_count:
                return True
            power_of_two *= 2
            str_power_of_two = str(power_of_two)

        return False