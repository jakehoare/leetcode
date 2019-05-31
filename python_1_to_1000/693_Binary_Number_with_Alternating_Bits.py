_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-number-with-alternating-bits/
# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always
# have different values.

# Repeatedly divide by 2 where remainder is bit value.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n, bit = divmod(n, 2)       # get first bit, avoids special case in while loop

        while n:

            if n % 2 == bit:        # next bit is same as current bit
                return False

            n, bit = divmod(n, 2)

        return True