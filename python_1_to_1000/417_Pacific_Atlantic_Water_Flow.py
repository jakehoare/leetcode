_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
# the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and
# bottom edges.  Water can only flow in four directions (up, down, left, or right) from a cell to another one with
# height equal or lower. Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Maintain a frontier of all cells that flow to each ocean, initially edges of matrix. Expand the frontier by adding
# all higher neighbours.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        atlantic, pacific = set(), set()        # cells that flow to each ocean

        for r in range(rows):
            atlantic.add((r, cols - 1))
            pacific.add((r, 0))
        for c in range(cols):
            atlantic.add((rows - 1, c))
            pacific.add((0, c))

        for ocean in [atlantic, pacific]:

            frontier = set(ocean)
            while frontier:
                new_frontier = set()
                for r, c in frontier:
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        r1, c1 = r + dr, c + dc     # neighbouring cell
                        if r1 < 0 or r1 >= rows or c1 < 0 or c1 >= cols or (r1, c1) in ocean:
                            continue                # ignore already found or outside matrix
                        if matrix[r1][c1] >= matrix[r][c]:  # nbor flows to ocean
                            new_frontier.add((r1, c1))
                frontier = new_frontier             # update frontier
                ocean |= new_frontier               # add newly discovered to ocean

        return list(atlantic & pacific)             # set intersection
