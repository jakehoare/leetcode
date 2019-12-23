_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# Given a m x n matrix mat and an integer threshold.
# Return the maximum side-length of a square with a sum less than or equal to threshold
# or return 0 if there is no such square.

# Iterate over matrix, converting each cell to the cumulative sum from (0, 0) to the cell.
# For each cell, if there is sufficient space to create a square of side length max_side + 1,
# find the sum of the square and increment max_side if the sum is <= threshold.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        max_side = 0

        def val_or_zero(row, col):      # return matrix value or 0 if not in matrix
            return mat[row][col] if row >= 0 and col >= 0 else 0

        for r in range(rows):
            for c in range(cols):
                mat[r][c] += val_or_zero(r - 1, c) + val_or_zero(r, c - 1) - val_or_zero(r - 1, c - 1)

                if r >= max_side and c >= max_side:
                    next_side_square = val_or_zero(r, c)
                    next_side_square -= val_or_zero(r - max_side - 1, c)
                    next_side_square -= val_or_zero(r, c - max_side - 1)
                    next_side_square += val_or_zero(r - max_side - 1, c - max_side - 1)
                    if next_side_square <= threshold:
                        max_side += 1

        return max_side
