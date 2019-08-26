_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
# Return the number of possible ways (out of f**d total ways) modulo 10^9 + 7
# to roll the dice so the sum of the face up numbers equals target.

# Dynamic programming.
# For each dice roll, each total can be achieved by adding any score s from 1 to f (inclusive)
# to total - s for the previous dice roll.
# Time - O(mnk) for target of m, n dice with k sides.
# Space - O(mn) for target of m and n dice.

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1                                    # 1 way to make 0 with 0 dice

        for die in range(1, d + 1):
            for total in range(die, target + 1):        # make each possible score
                dp[die][total] = sum(dp[die - 1][max(total - f, 0):total]) % MOD

        return dp[-1][-1]
