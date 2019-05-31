_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-uncommon-subsequence-i/
# Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence
# should not be any subsequence of the other strings.
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the
# order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.

# If the strings are identical then there is no uncommon subsequence. Else the longer string cannot be a subsequence of
# the shorter. If strings are same length but not identical they are uncommon subsequences of each other.
# Time - O(m + n)
# Space - O(1)

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))
