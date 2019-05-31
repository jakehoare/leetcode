_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/grid-illumination/
# On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.
# Initially, some number of lamps are on. lamps[i] tells us the location of the i-th lamp that is on.
# Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).
# For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.
# After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are
# adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)
# Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

# For each of the 4 directions (horizontal, vertical and 2 diagonals) count the number of lamps in each line.
# For each query call, sum the number of lamps shining on that cell across all 4 directions.
# If there is at least one lamp shining on the query cell, check the 9 cells in and around the query for lamps and
# decrement the count in each direction for each lamp found.
# Time - O(m + n), nb lamps + nb queries
# Space - O(m)

from collections import defaultdict

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lamps = {tuple(lamp) for lamp in lamps}                 # convert to set of O(1) lookup
        x_lamps, y_lamps = defaultdict(int), defaultdict(int)   # x_lamps[i] is the count of lamps with x-value of i
        up_diag_lamps, down_diag_lamps = defaultdict(int), defaultdict(int)

        for x, y in lamps:
            x_lamps[x] += 1
            y_lamps[y] += 1
            up_diag_lamps[x - y] += 1
            down_diag_lamps[x + y] += 1

        result = []
        for x, y in queries:
            illuminated = x_lamps[x] + y_lamps[y] + up_diag_lamps[x - y] + down_diag_lamps[x + y]
            result.append(min(illuminated, 1))                  # result of 1 if at least one lamp illuminating x, y

            if illuminated != 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if (x + dx, y + dy) in lamps:
                            lamps.discard((x + dx, y + dy))
                            x_lamps[x + dx] -= 1
                            y_lamps[y + dy] -= 1
                            up_diag_lamps[x + dx - y - dy] -= 1
                            down_diag_lamps[x + dx + y + dy] -= 1

        return result
