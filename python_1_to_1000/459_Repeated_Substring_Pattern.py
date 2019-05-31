_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/repeated-substring-pattern/
# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of
# the substring together. You may assume the given string consists of lowercase English letters only.

# If a string consists of 2 copies of a substring, then appending the string to itself and removing the first and last
# letters will still contain 2 copies of the substring. The same is true if there are more than 2 copies.
# Conversely, if the string is not a repeated substring then it cannot be built this way from 2 copies.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s in (s[1:] + s[:-1])