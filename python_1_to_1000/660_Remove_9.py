_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-9/
# Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...
# So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...
# Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.

# All remaining numbers without 9 are the base 9 numbers. Convert to base 9 by repeatedly dividing by 9, reverse result.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = []

        while n:
            result.append(str(n % 9))
            n //= 9

        return int("".join(result[::-1]))