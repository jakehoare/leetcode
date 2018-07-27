_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-triangle-area/
# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any
# 3 of the points.

# For each 3 points, use shoelace formula as per https://en.wikipedia.org/wiki/Shoelace_formula to calculate area.
# Time - O(n**3)
# Space - O(1)

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        largest = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]

                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    largest = max(largest, area)

        return largest