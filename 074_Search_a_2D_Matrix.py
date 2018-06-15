_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-a-2d-matrix/
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Treat the 2-d matrix as a 1-d list of length rows * cols. Binary search indices from 0 to rows * cols - 1.
# Time - O(log m + log n)
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
        low, high = 0, rows * cols - 1

        while high >= low:

            mid = (high + low) // 2
            value = matrix[mid // cols][mid % cols]     # convert mid to a row and column

            if target == value:
                return True
            if target > value:
                low = mid + 1
            else:
                high = mid - 1

        return False


