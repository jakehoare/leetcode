_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-right-interval/
# Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is
# bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.
# For any interval i, you need to store the minimum interval j's index, which means that the interval j has the
# minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for
# the interval i. Finally, you need output the stored value of each interval as an array.

# Sort tuples of intervals and original indices. For each interval, binary search for start point that is not less than
# end point.
# Time - O(n log n)
# Space - O(n)

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        intervals = [[intervals[i], i] for i in range(len(intervals))]
        intervals.sort(key=lambda x: x[0].start)

        result = [-1] * len(intervals)      # default to no right interval

        for interval, i in intervals:

            left, right = 0, len(intervals) # right = len(intervals) indicates no right interval

            while left < right:

                mid = (left + right) // 2
                if intervals[mid][0].start < interval.end:
                    left = mid + 1
                else:
                    right = mid

            if left == len(intervals):
                continue
            result[i] = intervals[left][1]

        return result
