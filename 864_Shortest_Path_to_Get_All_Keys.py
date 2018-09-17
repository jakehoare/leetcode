_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-path-to-get-all-keys/
# We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point,
# ("a", "b", ...) are keys, and ("A", "B", ...) are locks.
# We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.
# We cannot walk outside the grid, or walk into a wall. If we walk over a key, we pick it up.
# We can't walk over a lock unless we have the corresponding key.
# For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the
# English alphabet in the grid.
# This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used
# to represent the keys and locks were chosen in the same order as the English alphabet.
# Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.

# Find which keys are in the grid and the starting location. Breadth-first search the graph of states until all keys
# have been found. States consist of a location and sorted string of the keys found so far. In each cycle, every state
# in the frontier takes a step in all possible directions, potentially updating the locks acquired for the next state.
# Visited states are stored in a set so as not to be repeated.
# Time - O(mn * 2**k * k log k) for k keys
# Space - O(mn * k * 2**k)

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        possible_keys = set("abcdef")
        keys = set()

        for r in range(rows):                   # find the starting position and which keys are in the grid
            for c in range(cols):
                if grid[r][c] == "@":
                    start_r, start_c = r, c
                elif grid[r][c] in possible_keys:
                    keys.add(grid[r][c])

        steps = 0
        frontier = [(start_r, start_c, "")]     # states as tuples of (row, column, locks acquired)
        visited = set()
        neighbours = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while frontier:

            new_frontier = set()

            for r, c, open_locks in frontier:

                if (r, c, open_locks) in visited:    # ignore visited, outside grid, obstacle and locked doors
                    continue
                if r < 0 or r >= rows or c < 0 or c >= cols:
                    continue
                if grid[r][c] == "#":
                    continue
                if "A" <= grid[r][c] <= "F" and grid[r][c] not in open_locks:
                    continue

                visited.add((r, c, open_locks))

                if grid[r][c] in keys and grid[r][c].upper() not in open_locks:
                    open_locks = "".join(sorted(open_locks + grid[r][c].upper()))  # update sorted string of open locks

                if len(open_locks) == len(keys):
                    return steps

                for dr, dc in neighbours:
                    new_frontier.add((r + dr, c + dc, open_locks))

            frontier = new_frontier
            steps += 1

        return -1