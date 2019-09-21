_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-number-of-ones/
# Consider a matrix M with dimensions width * height, such that every cell has value 0 or 1,
# and any square sub-matrix of M of size sideLength * sideLength has at most maxOnes ones.
# Return the maximum possible number of ones that the matrix M can have.

# For each cell of the sub-matrix, count how many times that cell is repeated in the matrix.
# The count is equal to the number of times a cell appears in a row * the number of times a cell appears in a column.
# A cell appears in a row the number of times the sub-matrix is repeated along the width, adding 1 if the cell is in
# the remaining rows.
# Sort the number of times each cell appears, add ones to the maxOnes most frequent cells.
# Time - O(n**2 log n) for sideLength n
# Space - O(n**2)

class Solution(object):
    def maximumNumberOfOnes(self, width, height, sideLength, maxOnes):
        """
        :type width: int
        :type height: int
        :type sideLength: int
        :type maxOnes: int
        :rtype: int
        """
        whole_width, remainder_width = divmod(width, sideLength)
        whole_height, remainder_height = divmod(height, sideLength)

        matrix = []
        for r in range(sideLength):
            for c in range(sideLength):
                repeats = (whole_width + int(r < remainder_width)) * (whole_height + int(c < remainder_height))
                matrix.append(repeats)

        return sum(sorted(matrix, reverse=True)[:maxOnes])
