_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shift-2d-grid/
# Given a 2D grid of size n * m and an integer k. You need to shift the grid k times.
# In one shift operation:
# Element at grid[i][j] becomes at grid[i][j + 1].
# Element at grid[i][m - 1] becomes at grid[i + 1][0].
# Element at grid[n - 1][m - 1] becomes at grid[0][0].
# Return the 2D grid after applying shift operation k times.

# Build a new array by iterating over the indices of the existing array.
# Indices are from 0 to rows * cols - 1.
# For each index, find the shifted index - k modulo the number of indices.
# Convert that index to a row and column to find the value to append to the new array.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows, cols = len(grid), len(grid[0])
        n = rows * cols

        result = [[]]
        for i in range(n):                  # iterate over all indices of grid
            if len(result[-1]) == cols:     # make a new empty row
                result.append([])
            prev = (i - k) % n              # index of element to move here
            r, c = divmod(prev, cols)       # convert index in n to row and col
            result[-1].append(grid[r][c])

        return result
