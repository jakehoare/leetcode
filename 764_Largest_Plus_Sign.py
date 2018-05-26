_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-plus-sign/
# In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which
# are 0. What is the largest axis-aligned plus sign of 1s contained in the grid?
# Return the order of the plus sign. If there is none, return 0.
# An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up,
# down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s
# beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

# Iterate over the array by row in both directions and by column in both directions (4 times in total).
# In each direction, find the longest sequence of cells without a mine. Result for each cell is the the shortest
# distance in any of the 4 directions.
# Time - O(N**2)
# Space - O(N**2)

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mines = {(r, c) for r, c in mines}                      # convert to set for O(1) lookup
        distances = [[0 for _ in range(N)] for _ in range(N)]   # min distance to mine in each of the 4 directions
        plus = 0

        for r in range(N):
            distance = 0
            for c in range(N):
                distance = 0 if (r, c) in mines else distance + 1   # update distance since last mine
                distances[r][c] = distance

            distance = 0
            for c in range(N - 1, -1, -1):                          # reverse direction over rows
                distance = 0 if (r, c) in mines else distance + 1
                distances[r][c] = min(distances[r][c], distance)

        for c in range(N):
            distance = 0
            for r in range(N):
                distance = 0 if (r, c) in mines else distance + 1
                distances[r][c] = min(distances[r][c], distance)

            distance = 0
            for r in range(N - 1, -1, -1):
                distance = 0 if (r, c) in mines else distance + 1
                distances[r][c] = min(distances[r][c], distance)
                plus = max(plus, distances[r][c])

        return plus