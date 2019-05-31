_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-closest-points-to-origin/
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# Here, the distance between two points on a plane is the Euclidean distance.
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

# Build a heap of the K smallest distances from the origin.
# Time - O(n log k)
# Space - O(k)

import heapq

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(K, points, lambda x, y: x * x + y * y)
