_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rotting-oranges/
# In a given grid, each cell can have one of three values:
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1 instead.

# Breadth-first search. Create sets of coordinates of fresh and rotted oranges. While there are still some fresh,
# for each rotten orange, add any fresh neighbours to the set to be updated and add the rotten orange to the set of
# already checked oranges.
# For each minute, if there are no new rotten oranges and some fresh then not all oranges can be rotten.
# Else remove the checked oranges from rotten and convert newly rotted oranges from fresh to rotten.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        fresh, rotten = set(), set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                if grid[r][c] == 2:
                    rotten.add((r, c))

        mins = 0
        while fresh:
            mins += 1
            new_rotten = set()

            for r, c in rotten:
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:   # check all neighbours
                    if (r + dr, c + dc) in fresh:
                        new_rotten.add((r + dr, c + dc))

            if not new_rotten:
                return -1
            rotten = new_rotten
            fresh -= new_rotten

        return mins
