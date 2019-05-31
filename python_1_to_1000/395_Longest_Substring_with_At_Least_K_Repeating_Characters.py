_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every
# character in T appears no less than k times.

# Split string by all chars with frequency less than k. Repeat with substrings until all chars are present >= k times.
# Discard substrings shorter than current longest.
# Time - O(n**3), every while loop removes one char from original s, for every c in freq, splitting is O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        longest = 0
        to_split = [s]              # list of all substrings that may have infrequent chars

        while to_split:
            t = to_split.pop()      # any substring to be checked
            freq = Counter(t)
            splitted = [t]          # the result of removing all infrequent chars from t

            for c in freq:
                if freq[c] < k:     # split t by every infrequent character
                    new_splitted = []
                    for spl in splitted:
                        new_splitted += spl.split(c)
                    splitted = new_splitted

            if len(splitted) == 1:  # cound not be split, candicate for longest
                longest = max(longest, len(splitted[0]))
            else:                   # only add back candidates that are sufficiently long
                to_split += [spl for spl in splitted if len(spl) > longest]

        return longest