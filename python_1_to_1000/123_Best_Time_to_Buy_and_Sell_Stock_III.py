_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# As per problem 121 with an additional buy and sell.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1, buy2 = float('-inf'), float('-inf')
        sell1, sell2 = 0, 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, price + buy1)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, price + buy2)

        return sell2