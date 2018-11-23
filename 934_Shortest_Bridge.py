_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-bridge/
# In a given 2D binary array A, there are two islands.
# An island is a 4-directionally connected group of 1s not connected to any other 1s.
# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

# Traverse the grid until we any cell from an island. Then depth-first search to find all perimeter cells of the island
# which are at the edge of the island.  Breath-first search from the perimeter. Ignore cells that are already visited.
# Return when any island cell is found.
# Time - O(mn)
# Space - O(mn)

class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        rows, cols = len(A), len(A[0])
        visited = set()
        perimeter = set()

        def neighbours(r, c):       # yields cells neighbouring (r, c) that are within the grid A
            if r != 0:
                yield (r - 1, c)
            if r != rows - 1:
                yield (r + 1, c)
            if c != 0:
                yield (r, c - 1)
            if c != rows - 1:
                yield (r, c + 1)

        def get_perimeter(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if A[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))

            for r1, c1 in neighbours(r, c):
                if A[r1][c1] == 0:      # neighbours of an island cell that are not part of the island
                    perimeter.add((r1, c1))
                else:                   # recurse to explore island
                    get_perimeter(r1, c1)

        for r in range(rows):
            for c in range(cols):
                if perimeter:           # stop when any perimeter is found
                    break
                get_perimeter(r, c)

        steps = 1                       # perimeter is one step from the island

        while True:

            new_perimeter = set()
            for r, c in perimeter:
                for r1, c1 in neighbours(r, c):
                    if (r1, c1) in visited:
                        continue
                    if A[r1][c1] == 1:  # other island found
                        return steps
                    new_perimeter.add((r1, c1))

            visited |= new_perimeter
            perimeter = new_perimeter
            steps += 1
