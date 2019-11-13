_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.

# Find the initial slope between the first 2 points.
# If the slopes between the first point and all other points are the same as the initial slope, return True.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 3:    # 1 or 2 points are always on a line.
            return True

        x_diff = coordinates[1][0] - coordinates[0][0]  # keep diffs since gradient is a float
        y_diff = coordinates[1][1] - coordinates[0][1]

        for x, y in coordinates[2:]:
            dx = x - coordinates[0][0]
            dy = y - coordinates[0][1]
            if x_diff * dy != y_diff * dx:
                return False

        return True
