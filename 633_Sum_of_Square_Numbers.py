_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-square-numbers/
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# Incremetn a from 0 until 2 a**2 >= c. Check if b is an integer.
# Time - O(sqrt(n))
# Space - O(1)

from math import sqrt

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0

        while a <= sqrt(c / 2):

            b = sqrt(c - a ** 2)
            if int(b) == b:
                return True
            a += 1

        return False