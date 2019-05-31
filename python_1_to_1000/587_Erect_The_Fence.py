_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/erect-the-fence/
# There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to
# fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all
# the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence
# perimeter.

# Find the lowest point (most -ve y coordinate), breaking ties by most negative x-coordinate. Create a convex hull
# starting from this point. Sort other points by gradient, breaking ties with highest y coordinate then lowest x
# coordinate. For each point in sorted order (anti-clockwise around the hull), while the cross-product of this point
# and the last 2 points on the hull is negative, the 3 points turn clockwise so remove the last point from the hull.
# Time - O(n log n)
# Space - O(n)

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        if len(points) < 3:
            return points

        def slope(a, b):  # of line from a to b
            if a.x == b.x:
                return float("inf")
            return (b.y - a.y) / float(b.x - a.x)

        def cross_product(p):
            v1 = [result[-1].x - result[-2].x, result[-1].y - result[-2].y]
            v2 = [p.x - result[-2].x, p.y - result[-2].y]
            return v1[0] * v2[1] - v1[1] * v2[0]

        # find point with lowest x value, then lowest y value
        start_point = min(points, key=lambda p: (p.x, p.y))
        points.remove(start_point)

        # sort by slope, then closest (largest) y, then closest (smallest) x
        points.sort(key=lambda p: (slope(start_point, p), -p.y, p.x))

        result = [start_point, points[0]]

        for point in points[1:]:
            while cross_product(point) < 0:
                result.pop()
            result.append(point)

        return result

