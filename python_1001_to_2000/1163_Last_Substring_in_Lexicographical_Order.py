_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/last-substring-in-lexicographical-order/
# Given a string s, return the last substring of s in lexicographical order.

# Find all indices in s of the greatest char (lexicographically last).
# These are the stating indices of candidate substrings.
# While there is more than one candidate, find the next char and index of each candidate substring.
# Form the next chars, retain on the substrings with the greatest char.
# If the end of one candidate runs into the start of another candidate, reject the shorter candidate.
# Return the substring from the last remaining candidate to the end of s.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_char = max(s)
        candidates = {i for i in range(n) if s[i] == max_char}  # indices of max_char
        length = 0

        while len(candidates) > 1:
            char_indices = defaultdict(set)
            for i in candidates:
                if i == n - 1:
                    continue
                if i - length - 1 in candidates:    # another candidate runs into this candidate
                    continue
                char_indices[s[i + 1]].add(i + 1)

            candidates = char_indices[max(char_indices.keys())]
            length += 1

        return s[candidates.pop() - length:]        # suffix of s
