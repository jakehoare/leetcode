_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/
# In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1).
# The grid has empty cells represented by zeros and blocked cells represented by ones.
# The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).
# In one move the snake can:
# Move one cell to the right if there are no blocked cells there.
# This move keeps the horizontal/vertical position of the snake as it is.
# Move down one cell if there are no blocked cells there.
# This move keeps the horizontal/vertical position of the snake as it is.
# Rotate clockwise if it's in a horizontal position and the two cells under it are both empty.
# In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).
# Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty.
# In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).
# Return the minimum number of moves to reach the target.
# If there is no way to reach the target, return -1.

# Breadth-first search.
# Frontier consists of a set of states signifying the head position and whether the snake is horizontal.
# For each move, update the frontier with all possible next states depending on the orientation and whether
# neighbouring cells are in the grid and unoccupied.
# Set of seen states avoids repetition.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        moves = 0
        seen = set()
        frontier = {(0, 1, True)}  # (row of head, col of head, is horizontal)

        while frontier:
            if (rows - 1, cols - 1, True) in frontier:
                return moves

            new_frontier = set()
            for r, c, horizontal in frontier:
                if (r, c, horizontal) in seen:
                    continue

                if horizontal and c != cols - 1 and grid[r][c + 1] == 0:
                    new_frontier.add((r, c + 1, True))
                if not horizontal and r != rows - 1 and grid[r + 1][c] == 0:
                    new_frontier.add((r + 1, c, False))

                if horizontal and r != rows - 1 and grid[r + 1][c] == 0 and grid[r + 1][c - 1] == 0:
                    new_frontier.add((r + 1, c, True))          # down
                    new_frontier.add((r + 1, c - 1, False))     # clockwise rotation

                if not horizontal and c != cols - 1 and grid[r][c + 1] == 0 and grid[r - 1][c + 1] == 0:
                    new_frontier.add((r, c + 1, False))         # right
                    new_frontier.add((r - 1, c + 1, True))      # anti-clockwise rotation

            seen |= frontier
            frontier = new_frontier
            moves += 1

        return -1
