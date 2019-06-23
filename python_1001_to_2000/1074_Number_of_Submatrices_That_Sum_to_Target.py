_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# Given a matrix, and a target, return the number of non-empty submatrices that sum to target.
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some different coordinate
# for example, if x1 != x1'.

# Calculate the cumulative sums along each row.
# For each pair of columns, calculate the sumbmatrix sum between those columns from row 0 to each row.
# Check if any other submatrix sum can be subtracted from the current sum to reach target.
# Time - O(m**2 * n)
# Space - O(mn)

from collections import defaultdict

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        if rows < cols:             # swap rows and cols if more cols
            matrix = zip(*matrix[::-1])
            rows, cols = cols, rows

        cumulative_rows = []        # sum along each row
        for row in range(rows):
            cumulative_rows.append([matrix[row][0]])
            for col in range(1, cols):
                cumulative_rows[-1].append(matrix[row][col] + cumulative_rows[-1][-1])

        result = 0

        for col_start in range(cols):
            for col_end in range(col_start, cols):  # each pair of columns
                seen = defaultdict(int, {0: 1})     # count submatrix sums between there columns
                submatrix = 0
                for row in range(rows):
                    submatrix += cumulative_rows[row][col_end]  # add new row upto sol_end
                    if col_start != 0:
                        submatrix -= cumulative_rows[row][col_start - 1]    # subtract row before col_start

                    if submatrix - target in seen:
                        result += seen[submatrix - target]
                    seen[submatrix] += 1

        return result
