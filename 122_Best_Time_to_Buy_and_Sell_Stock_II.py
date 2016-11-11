_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple
# transactions at the same time (ie, you must sell the stock before you buy again).

# Sum all price increases.
# Time - O(n)
# Space - O(n), could be O(1) without creating a new list

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([max(prices[i]-prices[i-1], 0) for i in range(1,len(prices))])
