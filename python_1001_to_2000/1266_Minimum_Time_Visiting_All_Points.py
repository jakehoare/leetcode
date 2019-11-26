_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-time-visiting-all-points/
# On a plane there are n points with integer coordinates points[i] = [xi, yi].
# Your task is to find the minimum time in seconds to visit all points.
# You can move according to the next rules:
# In one second always you can either move vertically, horizontally by one unit or diagonally
# (which means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.

# To move between points take the maximum of the move in the x direction and the move in the y direction.
# This is because we can move diagonally to cover the move in the shorter direction,
# while also moving in the longer direction.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x1, y1 = points[0]          # current point
        time = 0

        for x2, y2 in points[1:]:
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            time += max(dx, dy)
            x1, y1 = x2, y2         # update current point

        return time
