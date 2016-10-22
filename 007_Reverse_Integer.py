_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-integer/
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Repeatedly multiply previous result by 10 and add last digit.
# Time - O(n) where n is the number of digits.
# Space - O(n), same number of digits in output as input.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0    # record if negative and change to positive
        x = abs(x)
        reversed = 0

        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10

        if reversed > 2**31 - 1:    # required to pass leetcode test cases, not applicable for python
            return 0
        return reversed if not negative else -reversed


