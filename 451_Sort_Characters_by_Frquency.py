_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-characters-by-frequency/
# Given a string, sort it in decreasing order based on the frequency of characters.

# Count frequency of chars and sort tuples of (-count, char) into frequency order.
# Time - O(n log n)
# Space - O(n)

from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s)
        pairs = [(count, c) for c, count in freq.items()]
        pairs.sort(reverse = True)

        result = []
        for count, c in pairs:
            result += [c] * count

        return "".join(result)