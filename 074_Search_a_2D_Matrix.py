_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-a-2d-matrix/
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Binary search first column to find the row, then binary search that row.
# Time - O(log m + log n)
# Space - O(max(log m, log n))

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])

        high, low = rows-1, 0

        while high >= low:
            mid = (high + low) // 2
            value = matrix[mid][0]
            if target == value:
                return True
            elif target > value:
                low = mid+1
            else:
                high = mid-1

        if high == -1:
            return False
        row = high

        high, low = cols-1, 0

        while high >= low:
            mid = (high + low) // 2
            value = matrix[row][mid]
            if target == value:
                return True
            elif target > value:
                low = mid+1
            else:
                high = mid-1

        return False
