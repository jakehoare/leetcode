_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-path-sum/
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
# the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# Dynamic programming, min path to a cell = cell value + min(min paths to cells above and left)
# Time - O(m * n)
# Space - O(m * n), could reduce to O(n) by keeping only previous row


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        min_path = [[float('inf') for col in range(n+1)] for row in range(m+1)]
        min_path[0][1] = 0

        for row in range(1, m+1):
            for col in range(1, n+1):
                min_path[row][col] = grid[row-1][col-1] + min(min_path[row-1][col], min_path[row][col-1])

        return min_path[-1][-1]