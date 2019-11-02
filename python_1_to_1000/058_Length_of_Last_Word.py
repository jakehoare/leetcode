_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/length-of-last-word/
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.

# Start at last character and decrement i.
# Set variable end when non-blank is seen.
# Return at next non-blank.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        end = -1

        while i >= 0:
            if s[i] == ' ' and end != -1:
                return end - i
            if s[i] != ' ' and end == -1:
                end = i
            i -= 1
        return end + 1 if end != -1 else 0
