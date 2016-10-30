_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insert-interval/
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Find all intervals strictly to the left and to the right of new interval.  If any intervals in between they
# overlap with newInterval.  If any overlap, update start of newInterval with start of first overlap and
# update end with end of last overlap.
# Time - O(n)
# Space - O(1)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = 0, len(intervals)-1
        while left < len(intervals) and intervals[left].end < newInterval.start:
            left += 1

        while right >= 0 and intervals[right].start > newInterval.end:
            right -= 1

        if left <= right:
            newInterval.start = min(newInterval.start, intervals[left].start)
            newInterval.end = max(newInterval.end, intervals[right].end)

        return intervals[:left] + [newInterval] + intervals[right+1:]
