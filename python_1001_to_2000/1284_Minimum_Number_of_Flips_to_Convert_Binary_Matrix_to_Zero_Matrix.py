_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
# Given a m x n binary matrix mat.
# In one step, you can choose one cell and flip it and all the four neighbours of it if they exist
# Flip is changing 1 to 0 and 0 to 1.
# A pair of cells are called neighboors if they share one edge.
# Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.
# Binary matrix is a matrix with all cells equal to 0 or 1 only.
# Zero matrix is a matrix with all cells equal to 0.

# Convert the matrix to a linear list of bool, by row.
# Create a mapping from each linear index to its neighbours in the matrix.
# Breadth-first search the matrix states.
# Frontier consists of reachable states.
# For each state in frontier, flip each cell and its neighbours to create a new state.
# Time - O(mn * 2 ** mn), since there are 2 ** mn states
# Space - O(mn * 2 ** mn)

from collections import defaultdict

class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        linear = []
        for row in mat:
            linear += [bool(cell) for cell in row]

        linear_nbors = defaultdict(list)    # map linear index to nbors
        for r in range(rows):
            for c in range(cols):
                i = r * cols + c
                linear_nbors[i].append(i)
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:   # within matrix only
                        j = (r + dr) * cols + (c + dc)
                        linear_nbors[i].append(j)

        frontier = {tuple(linear)}          # immutable tuple can be added to set
        steps = 0
        seen = set()                        # avoid repeating states

        while frontier:
            new_frontier = set()

            for state in frontier:
                if all(not v for v in state):       # found result
                    return steps

                if state in seen:
                    continue
                seen.add(state)

                for i in range(rows * cols):
                    new_state = list(state)
                    for nbor in linear_nbors[i]:
                        new_state[nbor] = not (new_state[nbor])
                    new_frontier.add((tuple(new_state)))

            steps += 1
            frontier = new_frontier

        return -1                           # no result
