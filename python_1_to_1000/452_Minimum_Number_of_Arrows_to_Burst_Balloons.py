_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the
# start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence
# the x-coordinates of start and end of the diameter suffice. Start is always smaller than end.
# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend
# bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot.
# An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be
# shot to burst all balloons.

# Sort by ending edge. Greedily shoot first ending edge, which bursts all balloons that start before or after that edge.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        arrows, last_arrow = 0, float("-inf")
        points.sort(key = lambda x: x[1])

        for start, end in points:

            if start > last_arrow:
                arrows += 1
                last_arrow = end

        return arrows