_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

# Starting from the highest bit that is set in n, whilst that bit is set ot the same value in both m and n then set it
# to that value in the result.  Stop when a bit is set differently in m and n.
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