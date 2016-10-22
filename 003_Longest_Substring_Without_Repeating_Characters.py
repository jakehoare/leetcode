_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.

# TODO SOLUTION
# Time - O(TODO)
# Space - O(TODO)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        start = 0
        longest = 0

        for i, c in enumerate(s):
            if c in last_seen:
                pass
            else:
