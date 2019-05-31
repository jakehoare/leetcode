_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/nth-digit/
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

# There are 9 digits of length 1, 2 * 90 of length 2, 3 * 900 of length 3 ... Find the length of the number containing
# the nth digit by subtracting all shorter length digits. Then divide n - 1 by length to get the number. Remainder is
# the required digit.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length = 1
        digits = 9

        while n > digits:
            n -= digits
            digits = (length + 1) * 9 * (10 ** length)
            length += 1

        start = 10 ** (length - 1)          # first number of this length
        num, digit = divmod(n - 1, length)
        num += start

        return int(str(num)[digit])