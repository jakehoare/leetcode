_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/contain-virus/
# A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.
# The world is modeled as a 2-D array of cells, where 0 represents uninfected cells, and 1 represents cells
# contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent
# cells, on the shared boundary.
# Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall.
# Resources are limited. Each day, you can install walls around only one region -- the affected area (continuous
# block of infected cells) that threatens the most uninfected cells the following night. There will never be a tie.
# Can you save the day? If so, what is the number of walls required? If not, and the world becomes fully infected,
# return the number of walls used.

# Iterate over grid, finding regions of virus with dfs. For each region find its empty neighbours and walls required
# to contain it. Contain the region with most neighbours by setting grid cells to 2 and increment wall count.
# Infect neighbours of of other regions. Repeat until no uninfected uncontained regions or no more infection possible.
# Time - O(mn * min(m, n)), mn for main loop, at most min(m, n) iterations since expansion by 1 row and col per round
# Space - O(mn)

class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        used_walls = 0

        def get_nbors(r, c):    # find all neighbouring empty cells and number of walls to contain a region
            if (r, c) in visited:
                return
            visited.add((r, c))

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                r1, c1 = r + dr, c + dc
                if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols:
                    continue
                if grid[r1][c1] == 2:       # ignore, already contained
                    continue
                if grid[r1][c1] == 0:       # add to nbors and increase wall count
                    nbors.add((r1, c1))
                    walls[0] += 1
                else:
                    get_nbors(r1, c1)       # recurse

        def contain_region(r, c):   # set all cells in a region to 2 to indicate contained
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != 1:
                return
            grid[r][c] = 2
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                contain_region(r + dr, c + dc)

        while True:
            regions = []
            visited = set()

            for r in range(rows):
                for c in range(cols):
                    # for each viral region, find its neighbouring empty cells and walls required
                    if (r, c) not in visited and grid[r][c] == 1:
                        nbors, walls = set(), [0]
                        get_nbors(r, c)
                        regions.append([(r, c), set(nbors), walls[0]])

            regions.sort(key = lambda x: -len(x[1]))        # sort by most neighbours

            if not regions or len(regions[0][1]) == 0:      # all contained or fully infected
                return used_walls

            used_walls += regions[0][2]                     # contain first region
            contain_region(regions[0][0][0], regions[0][0][1])

            for _, expansion, _ in regions[1:]:             # infect neighbours of other regions
                for r, c in expansion:
                    grid[r][c] = 1


