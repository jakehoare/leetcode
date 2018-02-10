_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.

# Maintain a sliding window, updating the start whenever we see a character repeated.
# Time - O(n)
# Space - O(1), dictionary is limited by fixed size alphabet

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}      # mapping from character to it's last seen index in s
        start = 0           # start index of current substring
        longest = 0

        for i, c in enumerate(s):

            if c in last_seen and last_seen[c] >= start:
                # start a new substring after the previous sighting of c
                start = last_seen[c]+1
            else:
                longest = max(longest, i-start+1)

            last_seen[c] = i    # update the last sighting index

        return longest
