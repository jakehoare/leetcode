_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
# Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.
# Suppose you triangulate the polygon into N-2 triangles.
# For each triangle, the value of that triangle is the product of the labels of the vertices,
# and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.
# Return the smallest possible total score that you can achieve with some triangulation of the polygon.

# Each edge forms a triangle with another vertex not along the edge.
# Recursively choose any edge (last vertex to first vertex) and build triangles with all other vertices. Add the
# product of the triangle vertices from the recursive results of the smaller left and right polygons. Memoize.
# Time - O(n**3)
# Space - O(n**2)

from functools import lru_cache

class Solution(object):
    def minScoreTriangulation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        @lru_cache(None)
        def helper(i, j):
            if j - i <= 1:
                return 0
            return min(helper(i, k) + A[i] * A[k] * A[j] + helper(k, j) for k in range(i + 1, j))

        return helper(0, len(A) - 1)
