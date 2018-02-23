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
        rows, cols = len(matrix), len(matrix[0])

        def bin_search(low, high, row):     # if row == -1 then search first values of rows
                                            # else search cols of a specific row
            while high >= low:

                mid = (high + low) // 2
                if row != -1:
                    value = matrix[row][mid]
                else:
                    value = matrix[mid][0]

                if target == value:
                    return -2               # signifies target is found
                elif target > value:
                    low = mid + 1
                else:
                    high = mid - 1

            return high

        row = bin_search(0, rows - 1, -1)
        if row == -2:
            return True
        if row == -1:
            return False

        return bin_search(0, cols - 1, row) == -2


