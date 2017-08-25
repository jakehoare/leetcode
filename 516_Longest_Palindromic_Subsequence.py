_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-palindromic-subsequence/
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length
# of s is 1000.

# Dynamic progrmming. Iterate over lengths. If end chars of substring of s of length l starting at index i are same,
# max length is 2 + max length without end chars. Else take max of leaving off one end char.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == s[::-1]:    # early return for palindromes
            return n

        subsequence_2 = [0 for _ in range(n)]   # subsequences of length - 2 for each starting index
        subsequence_1 = [1 for _ in range(n)]   # subsequences of length - 1 for each starting index

        for length in range(2, n + 1):
            subsequence = []
            for i in range(0, n - length + 1):

                if s[i] == s[i + length - 1]:
                    subsequence.append(2 + subsequence_2[i + 1])
                else:
                    subsequence.append(max(subsequence_1[i], subsequence_1[i + 1]))

            subsequence_2 = subsequence_1
            subsequence_1 = subsequence

        return subsequence[0]
