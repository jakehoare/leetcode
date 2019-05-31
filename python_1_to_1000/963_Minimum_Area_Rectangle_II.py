_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-area-rectangle-ii/
# Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points,
# with sides not necessarily parallel to the x and y axes.
# If there isn't any rectangle, return 0.

# Convert points to complex numbers for easier vector operations.
# Sort points so directions of vectors are aligned (else opposite directions are double counted).
# Map each vector between a pair to a list of mid-points of that vector.
# For each vector, if the vector between any pair of mid-points is perpendicular to the vector then a rectangle can
# be formed.
# Time - O(n**2)
# Space - O(n**2)

from collections import defaultdict
from itertools import combinations

class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        min_area = float("inf")

        points = [complex(*p) for p in sorted(points)]
        line_to_mid = defaultdict(list)

        for p1, p2 in combinations(points, 2):
            line_to_mid[p2 - p1].append((p1 + p2) / 2)

        for line1, mid_points in line_to_mid.items():
            for mid1, mid2 in combinations(mid_points, 2):

                line2 = mid2 - mid1
                if line1.real * line2.real + line1.imag * line2.imag == 0:
                    min_area = min(min_area, abs(line1) * abs(line2))

        return min_area if min_area != float("inf") else 0