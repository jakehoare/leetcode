_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Start at the top-right.  If target is greater than this value then it cannot be in this row so increment row.
# If target is less than this value then it cannot be in this column so decrement column.
# Time - O(m + n)
# Space - O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols-1

        while r < rows and c >= 0:

            if matrix[r][c] == target:
                return True

            if target > matrix[r][c]:
                r += 1
            else:
                c -= 1

        return False