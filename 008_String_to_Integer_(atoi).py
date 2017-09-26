_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/string-to-integer-atoi/
# Implement atoi to convert a string to an integer.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.

# Return the integer upto any non-digit.
# Time - O(n)
# Space - O(n), new str created by strip()


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()       # remove padding spaces

        negative = False        # remove leading + or -
        if str and str[0] == '-':
            negative = True
        if str and (str[0] == '+' or str[0] == '-'):
            str = str[1:]
        if not str:
            return 0

        digits = {i for i in '0123456789'}
        result = 0
        for c in str:           # record integer upto first non-digit
            if c not in digits:
                break
            result = result * 10 + int(c)

        if negative:
            result = -result

        result = max(min(result, 2**31 - 1), -2**31)    # keep within 4 byte signed integer bounds
        return result
