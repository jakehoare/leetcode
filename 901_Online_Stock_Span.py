_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/online-stock-span/
# Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's
# price for the current day.
# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and
# going backwards) for which the price of the stock was less than or equal to today's price.
# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85],
# then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

# Maintain a stack of descending prices and their spans. While the next price is greater than or equal to the previous
# price, remove the previous price from the stack and add its count to the result. Append the price and its span to
# the stack before returning the span.
# Time - O(n), worst case is everything must be popped off stack
# Space - O(n)

class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        result = 1                          # today's price has a span of 1

        while self.stack and price >= self.stack[-1][0]:
            _, count = self.stack.pop()
            result += count

        self.stack.append([price, result])
        return result

