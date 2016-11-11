_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distinct-subsequences/
# Given a string S and a string T, count the number of distinct subsequences of T in S.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.

# Dynamic programming.  For all prefixes of s and t calculate the number of sequences.  Base case is there is one was the
# empty string is a subsequence of any string.
# Time - O(m * n) where m = len(s) and n = len(t)
# Space - O(m)


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        prev_subsequences = [1 for _ in range(len(s)+1)]    # empty string is always one subsequence of any string

        for r in range(1, len(t)+1):                        # first r characters of t, t[:r]

            subsequences = [0 for _ in range(len(s)+1)]

            for c in range(r, len(s)+1):                    # first c chars of s, s[:c], if c < r then no possibilities

                subsequences[c] = subsequences[c-1]         # if t[:r] if a subsequence of s[:c-1] then it also is of s[:c]
                if s[c-1] == t[r-1]:                        # last chars match, add t[:r-1] subsequences of c[:r-1]
                    subsequences[c] += prev_subsequences[c-1]

            prev_subsequences = subsequences

        return prev_subsequences[-1]

