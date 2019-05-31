_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-uncommon-subsequence-ii/
# Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon
# subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any
# subsequence of the other strings.
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the
# order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.

# COunrt freq of each string. Sort list of keys by decreasing length. If key is not unique, add to seen set. Else if
# not a subsequence of any string already seen, return its length.
# Time - O(s * n**2) where s is max length of string and n is number of strings
# Space - O(sn)

from collections import Counter

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def is_subsequence(s, t):       # return True if s is a subsequence of t
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            if i == len(s):
                return True
            return False

        counts = Counter(strs)
        unique_strs = list(counts.keys())
        unique_strs.sort(key=len, reverse=True)
        seen = set()

        for s in unique_strs:

            if counts[s] == 1:
                if not any([is_subsequence(s, t) for t in seen]):
                    return len(s)
            else:
                seen.add(s)

        return -1