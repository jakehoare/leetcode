_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# You are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a
# non-negative integer fee representing a transaction fee.
# You may complete as many transactions as you like, but you need to pay the transaction fee for each sale.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.

# Track most cash after buying at current price and most cash after selling at current price. Most cash after buying is
# higher of previous most and cash after buying here = sell - price. Most cash after selling is higher of previous most
# and cash after selling here = buy + price - fee.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy, sell = float("-inf"), 0

        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price - fee)

        return sell
