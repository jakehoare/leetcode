_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-distinct-islands-ii/
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Count the number of distinct islands. An island is considered to be the same as another if they have the same
# shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction
# or up/down direction).

# Iterate over array, for each cell with 1 breadth-first search to find a list of all connected cells forming an island.
# For each of the 8 possible rotations and rotation + reflections, manipulate the island then translate so the top left
# cell of the enclosing rectangle is (0, 0). Sort the resulting cells and set the canonical representation to be the
# maximum.
# Time - O(mn * log(mn))
# Space - O(mn)

class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def BFS(base_r, base_c):

            grid[base_r][base_c] = 0    # set base cell as visited
            queue = [(base_r, base_c)]
            for r, c in queue:          # queue is extended during iteration

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r, new_c = r + dr, c + dc

                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 0
                        queue.append((new_r, new_c))

            canonical = []              # create a standard representation of the island

            for _ in range(4):          # make 8 shapes by rotation and rotation + reflection
                queue = [(c, -r) for r, c in queue]     # clockwise 90 degree rotation
                min_r, min_c = min([r for r, _ in queue]), min([c for _, c in queue])
                canonical = max(canonical, sorted([(r - min_r, c - min_c) for r, c in queue]))

                reflected = [(r, -c) for r, c in queue] # reflect
                min_r, min_c = min([r for r, _ in reflected]), min([c for _, c in reflected])
                canonical = max(canonical, sorted([(r - min_r, c - min_c) for r, c in reflected]))

            return tuple(canonical)     # tuple allows hashing in set

        islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                islands.add(BFS(r, c))

        return len(islands)