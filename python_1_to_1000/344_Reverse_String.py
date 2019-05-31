_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-string/
# Write a function that takes a string as input and returns the string reversed.

# Reverse with slice operator.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]