_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/roman-to-integer/
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

# Check for 2-character matches and if none there must be a single char match.
# Time - O(n) where len(s) = n
# Space - O(1)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        doubles = {'CM' : 900, 'CD' : 400, 'XC' : 90, 'XL' : 40, 'IX' :9, 'IV' : 4}
        singles = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

        integer = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and s[i:i+2] in doubles:
                integer += doubles[s[i:i+2]]
                i += 2
            else:
                integer += singles[s[i]]
                i += 1

        return integer