_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/factorial-trailing-zeroes/
# Given an integer n, return the number of trailing zeroes in n!.

# Every trailing zero is created by a factor of 5 (since there are many more factors of 2 that together make
# trailing zeroes).  Count the numbers in 1..n that are divisible by 5, then those divisible by 25 which have a
# second factor of 5, then 125 etc ...
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroes = 0
        power_of_5 = 5

        while power_of_5 <= n:
            zeroes += n // power_of_5
            power_of_5 *= 5

        return zeroes
