_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/coin-change/
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.

# Depth first search of the tree of coin combinations.  Explore first branch by removing as many of largest coin until
# zero balance (result) or then try removing next smallest coins.  Back up to decrement number of largest coin.
# Prune branches that cannot lead to an improved result.
# Time - O(c**d) where branching factor c is number of coins and d is depth of tree (amount / smallest coin)
# Space - O(c**d)

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse = True)
        self.result = float("inf")

        def dfs(largest_coin, remainder, used_coins):

            if remainder == 0:
                self.result = min(self.result, used_coins)

            for i in range(largest_coin, len(coins)):                   # try coins with largest first

                if remainder >= coins[i] * (self.result - used_coins):  # cannot improve on result
                    break
                if coins[i] <= remainder:                               # use this coin
                    dfs(i, remainder - coins[i], used_coins + 1)

        dfs(0, amount, 0)
        return self.result if self.result != float("inf") else -1