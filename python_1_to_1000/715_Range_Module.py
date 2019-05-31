_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/range-module/
# A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following
# interfaces in an efficient manner.
#  addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that
#    interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in
#    the interval [left, right) that are not already tracked.
#  queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is
#    currently being tracked.
#  removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval
#    [left, right).

# Maintain a list of points and whether all values from a point to the next are in a range. Binary search to find
# the insertion point of a new range. Query by checking all points between left and right are in range.
# Time - O(n) to add and remove, O(log n) to query
# Space - O(n)

import bisect

class RangeModule(object):
    def __init__(self):
        self.points = [0, 10 ** 9]  # list of points (not necessarily always ends of ranges after mergers)
        self.in_range = [False, False]  # is ends[i] and points to ends[i + 1] in a range

    def addRange(self, left, right, add=True):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        i = bisect.bisect_left(self.points, left)  # find insertion index of left in list of points
        if self.points[i] != left:  # if left does not exist in the list already
            self.points.insert(i, left)  # insert left to sorted list of points
            self.in_range.insert(i, self.in_range[i - 1])  # will be overwritten but required when inserting right

        j = bisect.bisect_left(self.points, right)
        if self.points[j] != right:
            self.points.insert(j, right)
            self.in_range.insert(j, self.in_range[j - 1])  # right is in_range if point before it was

        self.points[i:j] = [left]  # consolidate points i to (but excluding) j
        self.in_range[i:j] = [add]  # consolidate in_range

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i = bisect.bisect(self.points, left) - 1    # if left is a point then we include it, else get the previous point
        j = bisect.bisect_left(self.points, right)  # ony check points before right
        return all(self.in_range[i:j])

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.addRange(left, right, False)