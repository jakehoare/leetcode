_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/moving-average-from-data-stream/
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Circular array. Replace array at index i with next val, update total and increment i. When i reaches end of array,
# reset i to start of array.
# Time - O(n) where n == size for __init__(). O(1) for next().
# Space - O(n)

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.array = [None for _ in range(size)]    # sliding window contents
        self.i = 0                                  # next index of array to be updated
        self.total = 0                              # sum of array

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.array[self.i] is not None:          # subtract entry leaving window from total
            self.total -= self.array[self.i]
        self.total += val
        self.array[self.i] = val

        self.i = (self.i + 1) % len(self.array)

        count = len(self.array)                     # find number of entries
        if self.array[-1] is None:
            count = self.i

        return self.total / float(count)