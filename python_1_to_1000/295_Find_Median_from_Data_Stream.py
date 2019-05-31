_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-median-from-data-stream/
# Design a data structure that supports the following two operations:
#   void addNum(int num) - Add a integer number from the data stream to the data structure.
#   double findMedian() - Return the median of all elements so far.
# If the size of the list is even, median is the mean of the two middle values.

# Partition the numbers into 2 heaps containing half the numbers below (or equal to) median and half the numbers above
# (or equal to) median.  If the count of numners is odd, spare number is added to lower heap.  New numbers are
# added to lower heap if less than or equal to its max value, else to higher heap.  Then heaps are rebalanced to
# maintain the lower being at most 1 greater than higher.
# Time - O(log n) to addNum(), O(1) to findMedian()
# Space - O(n)

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lower = []     # lower half of numbers, and the extra num if count is odd
        self.higher = []    # higher half of numbers

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.lower or num <= -self.lower[0]:     # push onto appropriate heap
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.higher, num)

        if len(self.higher) > len(self.lower):          # rebalance if more than half on higher heap
            heapq.heappush(self.lower, -heapq.heappop(self.higher))
        elif len(self.lower) > 1 + len(self.higher):    # or more than half+1 on lower
            heapq.heappush(self.higher, -heapq.heappop(self.lower))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.lower) > len(self.higher):
            return float(-self.lower[0])
        return (-self.lower[0] + self.higher[0]) / 2.0
