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

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left, right = 0, len(intervals) - 1
        while left < len(intervals) and intervals[left][1] < newInterval[0]:
            left += 1

        while right >= 0 and intervals[right][0] > newInterval[1]:
            right -= 1

        if left <= right:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right][1])

        return intervals[:left] + [newInterval] + intervals[right + 1:]
