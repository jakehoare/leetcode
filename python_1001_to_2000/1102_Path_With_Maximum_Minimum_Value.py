_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-with-maximum-minimum-value/
# Given a matrix of integers A with R rows and C columns,
# find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].
# The score of a path is the minimum value in that path.
# For example, the value of the path 8 →  4 →  5 →  9 is 4.
# A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of
# the 4 cardinal directions (north, east, west, south).

# Maintain heap of (-score, row, column).
# Each cell is popped the heap and visited when it has its largest score.
# Add all neighbours within the grid bounds to the heap.
# Starting from [R-1, C-1] is faster than starting from [0, 0] because equal score ties are broken by lower row,
# which is closer to [0, 0].
# Time - O(mn log mn)
# Space - O(mn)

import heapq

class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        heap = [(-A[rows - 1][cols - 1], rows - 1, cols - 1)]

        while True:
            neg_max, r, c = heapq.heappop(heap)
            if A[r][c] == - 1:      # -1 signifies visited
                continue
            A[r][c] = -1
            if r == c == 0:
                return -neg_max
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                    continue
                heapq.heappush(heap, (max(-A[r + dr][c + dc], neg_max), r + dr, c + dc))
