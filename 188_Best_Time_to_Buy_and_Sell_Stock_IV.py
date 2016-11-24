_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Dynamic programming. Max profit after i buys = cost + max after i-1 transactions.
# Max profit after i sells = sale price + max after i-1 transactions and additional buy.
# Time - O(n * k)
# Space - O(n * k)

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k >= len(prices) // 2:       # can transact as often as required to get max profit
            return sum([max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))])

        # buys[i] is the max profit after i-1 buy/sell transactions and another buy
        # sells[i] is the max profit after i buy/sell transactions
        buys, sells = [float('-inf') for _ in range(k + 1)], [0 for _ in range(k + 1)]

        for price in prices:
            for i in range(1, len(buys)):

                buys[i] = max(buys[i], sells[i-1] - price)  # add -price to previous best after i-1 transactions
                if buys[i] == buys[i-1]:                    # additional transaction has not increased profit
                    break
                sells[i] = max(sells[i], buys[i] + price)   # add +price to max after i-1 transactions and another buy

        return max(sells)
