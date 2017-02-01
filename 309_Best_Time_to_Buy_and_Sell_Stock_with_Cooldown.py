_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

# Dynamic programming.  Max cash if last transaction was a buy is either the max cash after an earlier last buy or
# the max cash after an earlier sell at least 2 days ago and buying now.  The max cash after selling on a given day is
# either the max cash after an earlier last sell or the max cash after an earlier buy and selling now.
# Max cash after selling = max profit since the stock is no longer held.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell, prev_sell = float("-inf"), 0, 0

        for i, price in enumerate(prices):
            buy = max(buy, prev_sell-price)
            prev_sell = sell
            sell = max(sell, buy+price)
            print(buy, sell, prev_sell)

        return sell
