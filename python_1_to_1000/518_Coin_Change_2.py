_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/coin-change-2/
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount.
# You may assume that you have infinite number of each kind of coin.

# Dynamic programming. List stores the number of ways to make each amount. Use each coin in turn.
# For each amount >= the coin value, increment the number of ways to make that amount with the number of ways to
# make the amount - coin value.
# Time - O(mn) where m is the amount and n nis the number of coins
# Space - O(m)

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(amount + 1)]         # dp[i] nb ways to make i using no coins
        dp[0] = 1                                   # one way to make amount of zero

        for coin in coins:

            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]