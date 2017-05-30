_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/non-overlapping-intervals/
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
# intervals non-overlapping.
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

# Sort by increasing start point. If the next interval starts before the current end, set current end to be lesser of
# current and next ends. Else set current end to be next end if no overlap.
# Time - O(n log n)
# Space - O(1)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        erase = 0
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x.start)   # sort by increasing start
        current = intervals[0].start            # current interval end point

        for interval in intervals:

            if current > interval.start:  # overlap
                erase += 1
                if interval.end > current:  # retain current since end is less so less future overlaps
                    continue
            current = interval.end  # update current if no overlap or best choice

        return erase