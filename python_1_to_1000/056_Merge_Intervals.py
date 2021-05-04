_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-intervals/
# Given a collection of intervals, merge all overlapping intervals.

# Sort intervals by start points.  If interval starts before previous interval ends then merge, else add to result.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x : x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
