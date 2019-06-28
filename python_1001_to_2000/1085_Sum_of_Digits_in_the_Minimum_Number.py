_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/
# Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
# Return 0 if S is odd, otherwise return 1.

# Find the minimum and sum the digits.
# Time - O(n + log m) where n is the length of A and m is the minimum value.
# Space - O(1)

class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        minimum = min(A)
        digit_sum = 0
        while minimum:
            digit_sum += minimum % 10
            minimum //= 10
        return int(digit_sum % 2 == 0)
