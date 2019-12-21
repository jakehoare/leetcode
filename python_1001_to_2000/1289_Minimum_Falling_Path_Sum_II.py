_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-falling-path-sum-ii/
# Given a square grid of integers arr,
# a falling path with non-zero shifts is a choice of exactly one element from each row of arr,
# such that no two elements chosen in adjacent rows are in the same column.
# Return the minimum sum of a falling path with non-zero shifts.

# For each row, only the smallest and second smallest paths are used.
# Iterate over the rows, updating each element with the minimum sum path.
# For each row, each column is incremented by the smallest path from the previous row if the smallest path from
# the previous row is not the smallest, else is incremented by the second smallest path from the previous row.
# Time - O(mn)
# Space - O(mn)

import heapq

class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        n = len(arr)

        for row in range(1, n):
            smallest, second = heapq.nsmallest(2, arr[row - 1])
            for col in range(n):
                arr[row][col] += second if arr[row - 1][col] == smallest else smallest

        return min(arr[-1])
