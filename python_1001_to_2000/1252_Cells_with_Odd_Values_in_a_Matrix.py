_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices
# where indices[i] = [ri, ci].
# For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
# Return the number of cells with odd values in the matrix after applying the increment to all indices.

# Count whether the number of increments of each row and column is even or odd.
# For each cell, if the XOR of the row and column increments is odd then the value is odd.
# Time - O(k + mn) for k increments
# Space - O(m + n)

class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [True] * n       # True if even increments for each row
        cols = [True] * m       # True if even increments for each col

        for r, c in indices:
            rows[r] = not rows[r]
            cols[c] = not cols[c]

        result = 0
        for r in range(n):
            for c in range(m):
                result += int(rows[r] ^ cols[c])

        return result
