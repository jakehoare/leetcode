_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/integer-to-roman/
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.

# Repeatedly take of as many copies of each numeral as possible until num is less than
# the value of that numeral.
# Time - O(n) where n = len(str(num)), the longest roman equivalent is 8 where one digit maps to 4 chars
# Space - O(n)

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapping = [(1000, 'M'),
                    (900, 'CM'),
                    (500, 'D'),
                    (400, 'CD'),
                    (100, 'C'),
                    (90, 'XC'),
                    (50, 'L'),
                    (40, 'XL'),
                    (10, 'X'),
                    (9, 'IX'),
                    (5, 'V'),
                    (4, 'IV'),
                    (1, 'I'),]

        roman = []
        for i, numeral in mapping:
            while num >= i:
                num -= i
                roman.append(numeral)

        return "".join(roman)
