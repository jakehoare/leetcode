_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-boomerang/
# A boomerang is a set of 3 points that are all distinct and not in a straight line.
# Given a list of three points in the plane, return whether these points are a boomerang.

# Check if points are unique by calculating the length of the set of points.
# Points are a boomerang if the slopes between any 2 pairs of points are not equal.
# dx_1 / dy_1 != dx_2 / dy_2 but we multiply by dy_1 * dy_2 to avoid division by zero.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len({tuple(point) for point in points}) != 3:    # convert to tuple to allow use of set
            return False

        dx_1 = points[1][0] - points[0][0]
        dy_1 = points[1][1] - points[0][1]
        dx_2 = points[2][0] - points[0][0]
        dy_2 = points[2][1] - points[0][1]
        return dy_1 * dx_2 != dy_2 * dx_1
