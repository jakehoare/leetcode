_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-paths/
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Dynamic programming, nb paths = paths from above cell + paths from right cell
# Alternatively, catalan number.
# Time - O(m * n)
# Space - O(n), just keep last row instead of entire grid

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int    cols
        :type n: int    rows
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0

        row_paths = [1 for _ in range(n)]       # first row, one path to each column

        for row in range(m-1):
            new_row_paths = [1]                 # one path to first col of each row
            for col in range(1, n):
                new_row_paths.append(new_row_paths[-1] + row_paths[col])
            row_paths = new_row_paths

        return row_paths[-1]
