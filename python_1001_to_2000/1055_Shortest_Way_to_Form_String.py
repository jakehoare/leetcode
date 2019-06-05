_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-way-to-form-string/
# From any string, we can form a subsequence of that string by deleting some number of characters
# (possibly no deletions).
# Given two strings source and target, return the minimum number of subsequences of source such that
# their concatenation equals target.
# If the task is impossible, return -1.

# Create mapping from each source char to the indices in source of that char.
# Iterate over target, searching for the next index in source of each char. Return -1 if not found.
# Search is by binary search of the list of indices in source of char.
# If the next index in source requires wrapping around to the start of source, increment result count.
# Time - O(n log m) for source of length m and target of length n.
# Space - O(m)

from collections import defaultdict
import bisect

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        char_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_indices[c].append(i)

        result = 0
        i = 0                                       # next index of source to check

        for c in target:
            if c not in char_indices:               # cannot make target if char not in source
                return -1

            j = bisect.bisect_left(char_indices[c], i)  # index in char_indices[c] that is >= i
            if j == len(char_indices[c]):           # wrap around to beginning of source
                result += 1
                j = 0
            i = char_indices[c][j] + 1              # next index in source

        return result if i == 0 else result + 1     # add 1 for partial source
