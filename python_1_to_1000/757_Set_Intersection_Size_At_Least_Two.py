_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/set-intersection-size-at-least-two/
# An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.
# Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A
# has size at least 2.

# Sort intervals by ascending end point. Iterate over intervals. If the current interval starts after the previous
# intersection points then add to the intersection the end and end - 1. These are the maximum values in order to
# maximise overlaps with future intervals, which all end at the same or greater values. Or else if the second largest
# value in intersection is outside the interval, add the interval end point. Or else the last 2 values from intersection
# are included in interval so no action required.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        intersection = []

        for start, end in intervals:

            if not intersection or start > intersection[-1]:
                intersection.append(end - 1)
                intersection.append(end)
            elif start > intersection[-2]:
                intersection.append(end)
            # else previous 2 points in intersection are already in interval

        return len(intersection)
