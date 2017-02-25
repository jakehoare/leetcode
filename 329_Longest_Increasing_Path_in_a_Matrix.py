_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Given an integer matrix, find the length of the longest increasing path.
# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# For each starting cell, depth first search to explore all greater neighbours within the matrix.  Memoise results.
# Time - O(m * n)
# Space - O(m * n)

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        longest = 0
        memo = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                longest = max(longest, self.dfs(r, c, matrix, memo))
        return longest

    def dfs(self, r, c, matrix, memo):
        if memo[r][c] != -1:
            return memo[r][c]
        longest_here = 1        # can visit at least this cell
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= r + dr < len(matrix) and 0 <= c + dc < len(matrix[0]) and matrix[r + dr][c + dc] > matrix[r][c]:
                longest_here = max(longest_here, self.dfs(r + dr, c + dc, matrix, memo) + 1)
        memo[r][c] = longest_here
        return longest_here
