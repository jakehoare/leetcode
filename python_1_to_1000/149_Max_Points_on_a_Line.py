_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-points-on-a-line/
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# For each point, calculate the gradient of the line to all other points and store in dictionary.  Python accepts
# floats as dictionary keys and floating point accuracy is not an issue for sufficiently small x and y.
# Infinite slopes are stored with key of 'inf'.  If both x and y are the same, both points lie on all lines with the
# first point. Calculate the max number of points on a line with each base point in turn, only considering other points
# that have not already been the base point.
# Time - O(n**2)
# Space - O(n)

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        overall_max = 2

        for i, point in enumerate(points):  # for each point

            gradients = defaultdict(int)    # key is gradient, value is nb lines involving point with this gradient
            max_points = 1                  # point is on every line

            for point_2 in points[i+1:]:    # check all

                if point.x == point_2.x:
                    if point.y == point_2.y:    # same point, on all lines
                        max_points += 1
                    else:                       # infinite gradient
                        gradients['inf'] += 1

                else:
                    gradient = (point_2.y - point.y) / float(point_2.x - point.x)
                    gradients[gradient] += 1

            if gradients:
                max_points += max(gradients.values())
            overall_max = max(overall_max, max_points)

        return overall_max

