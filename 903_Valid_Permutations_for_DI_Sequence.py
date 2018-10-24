_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-permutations-for-di-sequence/
# We are given S, a length n string of characters from the set {'D', 'I'}.
# These letters stand for "decreasing" and "increasing".
# A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:
# If S[i] == 'D', then P[i] > P[i+1], and;
# If S[i] == 'I', then P[i] < P[i+1].
# How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

# Dynamic programming. For each character dp[i] is the number of results where the last number of the permutation is
# the i + 1th smallest amongst all numbers unused so far in that permutation (including that last number).
# If the next character is "D" then update dp[i] with the sum of all existing dp[j] where j > i, since we can move down
# from any solution where the final digit was ranked higher.
# Time - O(n**2)
# Space - O(n)

class Solution:
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1] * (len(S) + 1)     # dp[i] is nb solutions where the last number
                                    # is the i+1th smallest amongst all unused numbers
        for move in S:

            if move == "D":
                dp = dp[1:]         # move down from all last numbers apart from smallest
                for i in range(len(dp) - 2, -1, -1):
                    dp[i] += dp[i + 1]      # add all solutions with higher ranked last number
            else:
                dp = dp[:-1]        # move up from all last numbers apart from smallest
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]      # add all solutions with lower ranked last number

        return dp[0] % (10 ** 9 + 7)