_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/matrix-cells-in-distance-order/
# We are given a matrix with R rows and C columns has cells with integer coordinates (r, c),
# where 0 <= r < R and 0 <= c < C.
# Additionally, we are given a cell in that matrix with coordinates (r0, c0).
# Return the coordinates of all cells in the matrix,
# sorted by their distance from (r0, c0) from smallest distance to largest distance.
# Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.
# You may return the answer in any order that satisfies this condition.

# List all cells and sort by Manhattan distance from (r0, c0).
# Alternatively, breadth-first search maintaining a queue and ignoring cells outside matrix or already found.
# Time - O(mn log mn)
# Space - O(mn)

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        result = []
        for r in range(R):
            for c in range(C):
                result.append((r, c))

        return sorted(result, key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))


class Solution2(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        queue = deque()
        queue.append((r0, c0))
        result = []
        visited = set()

        while queue:

            r, c = queue.popleft()
            if r < 0 or r >= R or c < 0 or c >= C:
                continue
            if (r, c) in visited:
                continue

            result.append((r, c))
            visited.add((r, c))

            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                queue.append((r + dr, c + dc))

        return result
