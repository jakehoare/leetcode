_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/excel-sheet-column-number/
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For each char, multiply previous result by 26 and add value of char
# Time - O(n)
# Space - O(n)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            result = result*26 + ord(c) - ord('A') + 1
        return result