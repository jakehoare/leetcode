_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-window-substring/
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# Slide end of window forwards when not all letters in t are matched with window.  Slide start of window when all
# letters are matched.  Maintain the required count of each letter (can be negative if excess) and overall to_match.
# Time - O(n)
# Space - O(1)

from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq = Counter(t)
        best_start, best_end = 0, float('inf')
        start, end = 0, -1      # first and last indices of window in s
        to_match = len(t)

        while end < len(s)-1 or to_match == 0:      # can extend end or all matched so will increase start

            if to_match != 0:       # not all matched, extend end
                end += 1
                if s[end] in freq:  # reduce count, can be negative
                    freq[s[end]] -= 1
                    if freq[s[end]] >= 0:   # reduce to_match if count not negative
                        to_match -= 1

            else:                   # all matched, check if new min window, increment start
                if end - start < best_end - best_start:
                    best_end = end
                    best_start = start
                if s[start] in freq:    # add start letter back to count
                    freq[s[start]] += 1
                    if freq[s[start]] > 0:
                        to_match += 1   # increment to_match if positive count
                start += 1

        if best_end == float('inf'):
            return ''
        return s[best_start:best_end+1]
