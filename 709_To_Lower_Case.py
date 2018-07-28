_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/to-lower-case/
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# For each upper case character, convert to lower case by adding the ASCII code difference between lower and
# upper cases.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        diff = ord("a") - ord("A")

        return "".join(chr(ord(c) + diff) if "A" <= c <= "Z" else c for c in str)