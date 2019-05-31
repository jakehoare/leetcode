_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/group-shifted-strings/
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can
# keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same
# shifting sequence.

# For each string, shift so first character is "a". Map shifted string to list of all unshifted strings.
# Time - O(n), total number of chars of all strings
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        shifted = defaultdict(list)

        for s in strings:

            shift = ord(s[0]) - ord('a')            # assumes s is not empty
            s_shifted = "".join([chr((ord(c) - ord('a') - shift) % 26 + ord('a')) for c in s])
            shifted[s_shifted].append(s)

        return shifted.values()
