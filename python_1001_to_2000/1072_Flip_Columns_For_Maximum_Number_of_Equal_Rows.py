_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
# Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix
# and flip every cell in that column.
# Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.
# Return the maximum number of rows that have all values equal after some number of flips.

# For 2 rows to have all cells the same after some column flips, they must have either the same pattern of
# 0 and 1 or the opposite pattern.
# For each row, if the first column is not zero flip all values of that row by taking XOR with first value.
# Convert the row to a tuple and count the number of each tuple.
# The largest tuple count is the most rows that can be all equal.
# Time - O(mn)
# Space - O(mn)

from collections import defaultdict

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row_counter = defaultdict(int)
        for row in matrix:
            row_counter[tuple(x ^ row[0] for x in row)] += 1

        return max(row_counter.values())
