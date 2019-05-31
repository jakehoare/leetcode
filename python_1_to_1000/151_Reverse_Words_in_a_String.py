_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-words-in-a-string/
# Given an input string, reverse the string word by word.

# Parse int a list of words by spaces, reverse word list and recombine with spaces.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return " ".join(words[::-1])