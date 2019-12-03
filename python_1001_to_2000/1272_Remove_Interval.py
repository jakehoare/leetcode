_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-interval/
# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b]
# represents the set of real numbers x such that a <= x < b.
# We remove the intersections between any interval in intervals and the interval toBeRemoved.
# Return a sorted list of intervals after all such removals.

# Iterate over intervals.
# If remove_start is after the interval end, there is no overlap so append the interval to the result.
# If remove_end is before the interval start, there is no overlap and all other intervals will not overlap.
# Else if the start or end parts of the interval do not overlap, append them (possibly both) to the result.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        remove_start, remove_end = toBeRemoved
        result = []

        for i, (start, end) in enumerate(intervals):
            if remove_start >= end:
                result.append([start, end])
            elif remove_end <= start:       # all remaining intervals will not overlap
                result += intervals[i:]
                break
            else:
                if remove_start > start:
                    result.append([start, remove_start])
                if remove_end < end:
                    result.append([remove_end, end])

        return result
