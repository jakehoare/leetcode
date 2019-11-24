_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
# Given the following details of a matrix with n columns and 2 rows :
# The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i],
# where colsum is given as an integer array with length n.
# Your task is to reconstruct the matrix with upper, lower and colsum.
# Return it as a 2-D integer array.
# If there are more than one valid solution, any of them will be accepted.
# If no valid solution exists, return an empty 2-D array.

# Iterate along colsum.
# If colsum is 2, set both the upper and lower rows to 1 and decrement their required counts.
# If colsum is 1, set the row with the greatest required count to 1.
# If we have to set more than upper or lower, or have not set all required upper or lower at the end, return [].
# Time - O(n)
# Space - O(n)

class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        upper_row, lower_row = [0] * n, [0] * n     # default zeros

        for i, col in enumerate(colsum):

            if col == 2:
                lower -= 1
                upper -= 1
                upper_row[i] = lower_row[i] = 1
            elif col == 1 and upper > lower:        # set 1 in row with greatest required
                upper -= 1
                upper_row[i] = 1
            elif col == 1 and upper <= lower:
                lower -= 1
                lower_row[i] = 1

            if upper < 0 or lower < 0:
                return []

        if upper > 0 or lower > 0:
            return []
        return [upper_row, lower_row]
