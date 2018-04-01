_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ugly-number/
# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is
# not ugly since it includes another prime factor 7.
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range.

# Reject if <= 0. Remove all factors of 2, 3, and 5 then check if remainder is 1.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5

        return num == 1
