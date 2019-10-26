_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/dice-roll-simulation/
# A die simulator generates a random number from 1 to 6 for each roll.
# You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i]
# (1-indexed) consecutive times.
# Given an array of integers rollMax and an integer n,
# return the number of distinct sequences that can be obtained with exact n rolls.
# Two sequences are considered different if at least one element differs from each other.
# Since the answer may be too large, return it modulo 10^9 + 7.

# Dynamic programming. Find the number of sequences for each number of rolls and each final number.
# A sequence ending in j after i rolls can end in any number of j from 1 to rollMax[j].
# For each number k of sequence ending j, we can append [j] * k to any sequence of length i - k that does not end in j.
# Time - O(m n**2), for m sides and n rolls.
# Space - O(mn)

class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        sides = len(rollMax)
        # dp[i][j] is the number of ways we can end with a roll of j + 1 after i rolls
        dp = [[0 for j in range(sides)] for i in range(n + 1)]
        dp_total = [0] * (n + 1)  # dp_total[i] is the sum over j of dp[i][j]

        dp_total[0], dp_total[1] = 1, 6
        for j in range(sides):
            dp[1][j] = 1

        for i in range(2, n + 1):
            for j in range(sides):
                for k in range(1, rollMax[j] + 1):  # number of consecutive rolls of j at end of sequence
                    if i - k < 0:
                        break
                    dp[i][j] += dp_total[i - k] - dp[i - k][j]  # sequences of length i - k that do not end in k
            dp_total[i] = sum(dp[i])

        return dp_total[n] % (10 ** 9 + 7)
