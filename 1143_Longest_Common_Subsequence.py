_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-common-subsequence/
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
# Eg, "ace" is a subsequence of "abcde" while "aec" is not.
# A common subsequence of two strings is a subsequence that is common to both strings.
# If there is no common subsequence, return 0.

# Dynamic programming.
# For each prefix of text1, find the lcs with each prefix of text2.
# If the end characters of each prefix are equal, we can extend the lcs of the prefixes without the end characters.
# Else we take the longest lcs ignoring the last character from one prefix.
# Time - O(mn)
# Space - O(n)

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        lcs = [0 for _ in range(n + 1)]

        for c1 in text1:            # for prefix of text1 up to and including c1
            new_lcs = [0]
            for j, c2 in enumerate(text2):  # for prefix of text2 up to and including c2
                if c1 == c2:
                    new_lcs.append(1 + lcs[j])
                else:
                    new_lcs.append(max(new_lcs[-1], lcs[j + 1]))
            lcs = new_lcs

        return lcs[-1]

