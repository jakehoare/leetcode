_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/the-skyline-problem/
# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from
# a distance. Now suppose you are given the locations and height of all the buildings as a cityscape photo.
# Write a program to output the skyline formed by these buildings collectively.
# The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri
# are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height.
# It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are
# perfect rectangles grounded on an absolutely flat surface at height 0.

# Iterate over a sorted list of all left and right edges. Heap stores (-building height, right edge) whenever we
# see a left edge. For each edge, pop of all the buildings to the left, if it's a left edge then add the right 
# edge to the heap, record the highest building. Heap top has the highest 'alive' building after each edge.
# Time - O(n * logn), each building is inserted and removed from heap
# Space - O(n)

import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        skyline = [(0, 0)]              # resulting list of points, dummy first point
        current = [(0, float('inf'))]   # heap of 'alive' buildings by height, then by right edge

        edges = [(l, -h, r) for l, r, h in buildings]       # left edges
        edges += [(r, 0, None) for _, r, _ in buildings]    # right edges
        edges.sort()

        for x, neg_h, r in edges:

            while current[0][1] <= x:       # discard right edges that are left or equal to new edge
                heapq.heappop(current)      # dummy right edge at infinity ensures heap will never be empty

            if neg_h != 0:                  # implies left edge (since h will not be zero), push right edge
                heapq.heappush(current, (neg_h, r))

            if skyline[-1][1] != -current[0][0]:        # previous skyline different from highest alive building
                skyline.append([x, -current[0][0]])     # add point (x, highest 'alive' bldg) to result

        return skyline[1:]

