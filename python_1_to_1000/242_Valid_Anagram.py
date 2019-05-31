_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-anagram/
# Given two strings s and t, write a function to determine if t is an anagram of s.
# You may assume the string contains only lowercase alphabets.

# Strings s and t must contain the same number of each character.
# Time - O(m + n)
# Space - O(1)

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)