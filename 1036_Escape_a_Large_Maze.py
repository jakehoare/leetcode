_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/escape-a-large-maze/
# In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.
# We start at the source square and want to reach the target square.
# Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the list of blocked squares.
# Return true if and only if it is possible to reach the target square through a sequence of moves.
# 0 <= blocked.length <= 200

# Compress the grid so that gaps between populated rows and columns are at most one square wide.
# Then perform breadth-first search.
# Time - O(1) since there are at most 200 blocked squares.
# Space - O(1)

class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        # make sorted lists of all rows and cols used in blocked, source or target
        rows, cols = set(), set()
        for r, c in blocked + [source, target]:
            rows.add(r)
            cols.add(c)
        rows, cols = sorted(list(rows)), sorted(list(cols))

        # map original rows and cols to compressed values that reduce gaps to 1 element
        row_to_compressed, col_to_compressed = {}, {}
        new_row, new_col = int(rows[0] != 0), int(cols[0] != 0)  # add a gap if not starting at row or col zero

        for i, r in enumerate(rows):
            if i != 0 and rows[i - 1] != r - 1:  # not consecutive, add a gap of a single row
                new_row += 1
            row_to_compressed[r] = new_row
            new_row += 1

        for i, c in enumerate(cols):
            if i != 0 and cols[i - 1] != c - 1:  # not consecutive, add a gap of a single col
                new_col += 1
            col_to_compressed[c] = new_col
            new_col += 1

        # map the original inputs to their compressed values
        blocked = {(row_to_compressed[r], col_to_compressed[c]) for r, c in blocked}
        source = (row_to_compressed[source[0]], col_to_compressed[source[1]])
        target = (row_to_compressed[target[0]], col_to_compressed[target[1]])

        # set an extra row or col if we are not at the edege of the original grid
        if new_row != 10 ** 6 + 1:
            new_row += 1
        if new_col != 10 ** 6 + 1:
            new_col += 1

        # breadth first search
        frontier, back, visited = {source, }, {target, }, set()
        while frontier and back:

            if frontier & back - blocked:   # overlap between back and frontier that is not blocked
                return True
            if len(frontier) > len(back):   # expand smaller of frontier and back
                frontier, back = back, frontier
            new_frontier = set()

            for r, c in frontier:
                if (r, c) in blocked or (r, c) in visited:
                    continue
                if r < 0 or r >= new_row or c < 0 or c >= new_col:
                    continue

                visited.add((r, c))
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    new_frontier.add((r + dr, c + dc))

            frontier = new_frontier

        return False
