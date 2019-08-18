_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-1-bordered-square/
# Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s
# on its border, or 0 if such a subgrid doesn't exist in the grid.

# Iterate along each row, counting the continuous sequence of ones.
# For each side length from the sequence down to the current best side length + 1,
# check if the other 3 edges of the square are all ones.
# Return early or continue if the current best cannot be improved.
# Time - O(mn * (m + n)) since for each cell of the grid, explore up to side lengths of the grid.
# Space - O(1)

class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        best = 0

        for row in range(rows):
            sequence = 0
            for col in range(cols):
                if best >= rows - row:  # insufficient rows to make a bigger square
                    return best * best

                if grid[row][col] == 1:
                    sequence += 1
                else:
                    sequence = 0
                if best >= sequence :  # insufficient sequence to make a bigger square
                    continue

                for side in range(min(sequence, rows - row), best, -1): # check decreasing side from largest possible
                    if not all(grid[r][col] and grid[r][col - side + 1] for r in range(row + 1, row + side)):
                        continue    # left and right edges must be populated
                    if not all(grid[row + side - 1][col - side + 1:col + 1]):
                        continue    # bottom edge must be populated
                    best = side
                    break           # no need to check smaller sides

        return best * best

