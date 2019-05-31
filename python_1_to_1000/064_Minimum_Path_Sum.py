_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-path-sum/
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
# the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Dynamic programming, min path to a cell = cell value + min(min paths to cells above and left)
# Time - O(m * n)
# Space - O(n)

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        min_path = [float('inf') for _ in range(n + 1)]
        min_path[1] = 0

        for row in range(1, m + 1):
            new_min_path = [float('inf') for _ in range(n + 1)]
            for col in range(1, n + 1):
                new_min_path[col] = grid[row - 1][col - 1] + min(min_path[col], new_min_path[col - 1])
            min_path = new_min_path

        return min_path[-1]