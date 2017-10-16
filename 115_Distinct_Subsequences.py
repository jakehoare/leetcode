_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distinct-subsequences/
# Given a string S and a string T, count the number of distinct subsequences of T in S.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.

# Dynamic programming.  For all prefixes of S and T calculate the number of sequences.  Base case is that the prefix
# of T is the empty string, which is one subsequence of every prefix of S.
# The number of time T[:r] is a subsequence of S[:c] is the number of time T[:r] is a subsequence of S[:c - 1], plus
# if the last chars of T[:r] and S[:c] match then every T[:r - 1] subsequence of S[:c] can also be extended.
# empty string is a subsequence of any string.
# Time - O(m * n) where m = len(S) and n = len(T)
# Space - O(m)


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        prev_subsequences = [1 for _ in range(len(s) + 1)]    # empty string is always one subsequence of any string

        for r in range(1, len(t) + 1):                        # first r characters of T, i.e. T[:r]

            subsequences = [0 for _ in range(len(s) + 1)]

            for c in range(r, len(s) + 1):                    # first c chars of S. If c < r then no possibilities

                subsequences[c] = subsequences[c - 1]         # all T[:r] subsequences of S[:c - 1] are also
                                                              # subsequences of S[:c]
                if s[c - 1] == t[r - 1]:                      # last chars match, add T[:r-1] subsequences of S[:c-1]
                    subsequences[c] += prev_subsequences[c - 1]

            prev_subsequences = subsequences

        return prev_subsequences[-1]

