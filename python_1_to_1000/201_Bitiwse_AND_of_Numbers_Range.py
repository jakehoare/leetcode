_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Starting from the most significant bit that is set in n, compare each bit in n to the equivalent bit in m.
# If both bits are the same, set the same bit in the result to its value in m and n.
# Stop when a bit is set differently in m and n.
# When any bit is different, all less significant bits must take on both values of 0 and 1 in the range.
# Time - O(log n)
# Space - O(1)

from math import log

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        result = 0

        bit = int(log(n, 2))        # highest bit that is set in n

        while bit >= 0 and ((m  & (1 << bit)) == (n  & (1 << bit))):
            if (m  & (1 << bit)):   # if this bit is set
                result += 2**bit
            bit -= 1

        return result