_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
# whitespace and initial word order.

# Split string by space into a list of words. Reverse each word. Join reversed words by spaces.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([w[::-1] for w in s.split(" ")])