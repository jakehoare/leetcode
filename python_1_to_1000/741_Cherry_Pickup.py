_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/cherry-pickup/
# In a N x N grid representing a field of cherries, each cell is one of three possible integers.
#  0 means the cell is empty, so you can pass through;
#  1 means the cell contains a cherry, that you can pick up and pass through;
#  -1 means the cell contains a thorn that blocks your way.
# Your task is to collect maximum number of cherries possible by following the rules below:
#  Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells
#    (cells with value 0 or 1);
#  After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
#  When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
#  If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

# Instead of one person traversing there and back, consider two persons traversing simultaneously.
# The column of the second person is fixed by the position of the first person (which determines the number of steps
# taken) and the row of the second person, since both have taken the same number of steps.
# Top-down dynamic programming with 3 degrees of freedom. There are 4 cases of each person moving down or across.
# Time - O(n**3)
# Space - O(n**3)

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        memo = {}

        def helper(r1, c1, r2):

            c2 = r1 + c1 - r2

            if r1 == n or c1 == n or r2 == n or c2 == n:    # out of bounds
                return float("-inf")
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:    # either person is on a thorn
                return float("-inf")

            if r1 == n - 1 and c1 == n - 1:                 # both paths at end cell
                return grid[n - 1][n - 1]

            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]

            result = grid[r1][c1]                           # cherry from first person
            if r2 != r1 or c2 != c1:                        # if people not in same position
                result += grid[r2][c2]                      # add cherry from second person

            result += max(helper(r1 + 1, c1, r2 + 1), helper(r1, c1 + 1, r2),
                          helper(r1 + 1, c1, r2), helper(r1, c1 + 1, r2 + 1))

            memo[(r1, c1, r2)] = result
            return result

        return max(0, helper(0, 0, 0))                      # convert -inf (no solution) to zero

