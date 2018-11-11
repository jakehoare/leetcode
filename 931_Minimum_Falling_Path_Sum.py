_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-falling-path-sum/
# Given a square array of integers A, we want the minimum sum of a falling path through A.
# A falling path starts at any element in the first row, and chooses one element from each row.
# The next row's choice must be in a column that is different from the previous row's column by at most one.

# Dynamic programming. For each row from the bottom upwards, find the minimum falling path sum from each cell.
# The minimum from any cell is the value of that cell plus the minimum of the results from the 3 cells in the row below.
# Time - O(n**2)
# Space - O(n)

class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        row_minima = [0] * n

        for r in range(n - 1, -1, -1):      # from bottom row upwards

            new_row_minima = list(A[r])     # initilaise minimum path sums with the value of each cell

            for c in range(n):
                new_row_minima[c] += min(row_minima[max(0, c - 1):c + 2])   # add the lowest of the 3 cells below

            row_minima = new_row_minima

        return min(row_minima)              # start from any cell of top row
