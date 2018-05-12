_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-boomerangs/
# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that
# the distance between i and j equals the distance between i and k (the order of the tuple matters).
# Find the number of boomerangs.

# For each point, calculate the distances to all other points and create a mapping from each distance to the number of
# points with that distance. For each distance, calculate the the number of ways that the points at that distance
# can mane a boomerang, which is the number of pairs of points.
# Time - O(n**2)
# Space - O(n**2)

from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def dist_squared(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        boomerangs = 0

        for middle in points:
            distances = defaultdict(int)

            for i, other in enumerate(points):
                distances[dist_squared(middle, other)] += 1

            for count in distances.values():
                boomerangs += count * (count - 1)

        return boomerangs