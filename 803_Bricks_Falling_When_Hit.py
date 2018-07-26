_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bricks-falling-when-hit/
# We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will not drop if and only if it is directly
# connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.
# We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j),
# the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.
# Return an array representing the number of bricks that will drop after each erasure in sequence.

# Add all hits to grid, differentiating between those that hit a brick and those that are empty. Depth-first from the
# top row to flag all bricks that are still attached. Add back each brick in reverse order. If a brick added back has a
# neighbour that is attached, attach it and all connected bricks that are not already attached.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        rows, cols = len(grid), len(grid[0])
        nbors = ((1, 0), (0, 1), (-1, 0), (0, -1))

        for r, c in hits:  # set to zero if a brick was hit, else set to -1
            grid[r][c] -= 1

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] != 1:
                return 0
            grid[row][col] = 2
            return 1 + sum(dfs(row + dr, col + dc) for dr, dc in nbors)

        for c in range(cols):
            dfs(0, c)

        def connected(r, c):
            if r == 0:
                return True
            return any(0 <= (r + dr) < rows and 0 <= (c + dc) < cols \
                       and grid[r + dr][c + dc] == 2 for dr, dc in nbors)

        result = []
        for r, c in reversed(hits):
            grid[r][c] += 1
            if grid[r][c] == 1 and connected(r, c):
                result.append(dfs(r, c) - 1)  # ignore erased brick
            else:
                result.append(0)

        return result[::-1]

