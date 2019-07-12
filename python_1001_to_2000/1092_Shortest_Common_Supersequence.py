_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-common-supersequence/
# Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
# If multiple answers exist, you may return any of them.
# A string S is a subsequence of string T if deleting some number of characters from T
# (possibly 0, and the characters are chosen anywhere from T) results in the string S.

# Find the longest common supersequence by dynamic programming.
# For each pair of prefixes str1[:i] and str2 [:j], extend the result for i - 1, j - 1 if end chars are the same.
# Else take the larger result of i - 1, j and i, j - 1.
# Make the shortest common supersequence by iterating over the LCS.
# Add all chars of str1 to the result until we match a char in LCS. Do the same for str2, then add the matching char.
# Time - O(mn * min(m, n)) since there are O(mn) entries in the lcs matrix and each takes min(m, n) to build.
# Space - O(mn)

class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m, n = len(str1), len(str2)
        lcs = [["" for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    lcs[i + 1][j + 1] = lcs[i][j] + str1[i]
                else:
                    lcs[i + 1][j + 1] = max(lcs[i + 1][j], lcs[i][j + 1], key=len)

        result = []
        i, j = 0, 0
        for c in lcs[-1][-1]:
            while str1[i] != c:
                result.append(str1[i])
                i += 1
            while str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)    # add the lcs char
            i += 1
            j += 1

        return "".join(result) + str1[i:] + str2[j:]    # add remainders of str and str2
