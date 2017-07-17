_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convex-polygon/
# Given a list of points that form a polygon when joined sequentially, find if this polygon is convex.
# There are at least 3 and at most 10,000 points.
# Coordinates are in the range -10,000 to 10,000.
# You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other
# words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.

# For each edge, calculate cross product with previous edge. All cross products must have same sign to be convex.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        points.append(points[0])  # close the polygon by appending first edge to end
        points.append(points[1])  # ditto
        previous = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
        previous_cross = 0

        for i in range(2, len(points)):

            vector = [points[i][0] - points[i - 1][0], points[i][1] - points[i - 1][1]]
            cross_product = vector[0] * previous[1] - vector[1] * previous[0]

            if cross_product != 0:
                if previous_cross * cross_product < 0:
                    return False
                previous_cross = cross_product

            previous = vector

        return True