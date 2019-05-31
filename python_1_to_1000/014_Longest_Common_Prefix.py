_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.

# Sort strings and find longest prefix of first and last, which are the most different.
# Alternatively all strings could be inserted into a trie and we find the first node
# with more than one child.
# Time - O(k*n logn) where k is the length of the longest string and n is number of strings.
# Space - O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]
