_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/is-subsequence/
# Given a string s and a string t, check if s is subsequence of t.
# You may assume that there is only lower case English letters in both s and t. t is potentially a very long
# (length ~= 500,000) string, and s is a short string (<=100).

# Iterate over t looking for first char of s.  When found continue iteration over t looking for next char of s.
# Alternatively if many different s, create lists if indices of each char in t then binary search list for each char of
# s to find index in t after previous index in t.
# Time - O(n) when len(t) = n
# Space - O(1)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0           # next char to match in s
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False