_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.

# Record the max cash after buying stock at any point previously (which is negative), and the max cash after selling
# as the cash after boying + sale proceeds.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = float('-inf')     # maximum cash balance after buying a stock
        sell = 0                # maximum cash balance after buying and selling a stock

        for price in prices:
            buy = max(-price, buy)          # max of buying earlier or now
            sell = max(price + buy, sell)   # max of selling earlier or now

        return sell
