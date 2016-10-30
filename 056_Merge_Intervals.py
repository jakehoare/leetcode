_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-intervals/
# Given a collection of intervals, merge all overlapping intervals.

# Sort intervals by start points.  If interval starts before previous interval ends then merge, else add to result.
# Time - O(n log n)
# Space - O(1)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x : x.start)
        merged = []

        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged