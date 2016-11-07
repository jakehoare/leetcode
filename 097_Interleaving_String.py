_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/interleaving-string/
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# If the next char of s1 or s2 matches s3, recurse on the remainder.
# Time - O(m * n), every prefix of s1 * every prefix of s2
# Space - O(m * n)

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):    # early return
            return False
        return self.helper(s1, s2, s3, 0, 0, {})


    def helper(self, s1, s2, s3, i, j, memo):   # i, j are indices of next char to be matched in s1, s2

        if i >= len(s1) or j >= len(s2):        # base case, one string already matched
            return s1[i:] + s2[j:] == s3[i+j:]

        if (i, j) in memo:
            return memo[(i, j)]

        result = False
        if s1[i] == s3[i+j] and self.helper(s1, s2, s3, i+1, j, memo):
            result = True
        elif s2[j] == s3[i+j] and self.helper(s1, s2, s3, i, j+1, memo):
            result = True

        memo[(i, j)] = result
        return result
