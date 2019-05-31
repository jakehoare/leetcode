_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/magic-squares-in-grid/
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column,
# and both diagonals all have the same sum.
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

# Iterate over all possible top left corners of 3 x 3 squares. Reject if centre is not 5 or any number outside [0, 9].
# In each square, sum the rows, columns and diagonals.
# Time - O(mn)
# Space - O(1)

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic(row, col):

            if grid[row + 1][col + 1] != 5:     # centre must be 5
                return False

            line_sums = [0 for _ in range(6)]   # line_sums[:3] are sums of rows, line_sums[3:] are sums of cols
            diag1, diag2 = 0, 0                 # descending and ascending diagonal

            for dr in range(3):
                for dc in range(3):

                    val = grid[row + dr][col + dc]
                    if val < 1 or val > 9:      # reject if number outside range
                        return False

                    line_sums[dr] += val        # incerement all sums using this cell
                    line_sums[dc + 3] += val
                    if dr == dc:
                        diag1 += val
                    if dr + dc == 2:
                        diag2 += val

            if any(line_sum != 15 for line_sum in line_sums):
                return False
            if diag1 != 15 or diag2 != 15:
                return False
            return True

        rows, cols = len(grid), len(grid[0])
        magic = 0

        for r in range(rows - 2):
            for c in range(cols - 2):
                magic += is_magic(r, c)

        return magic