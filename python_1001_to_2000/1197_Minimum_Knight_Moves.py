_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-knight-moves/
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
# A knight has 8 possible moves it can make.
# Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# Return the minimum number of steps needed to move the knight to the square [x, y].
# It is guaranteed the answer exists.

# A-star search the board.
# Maintain a heap of positions, repeatedly expanding the position with the lowest possible result.
# Use a heuristic of the minimum possible moves to reach the target.
# If the distance in the smallest dimension (x or y) is less than twice the distance in the largest dimension,
# then we can potentially reach target in (largest dimension + 1) // 2 steps. Else we need to add additional steps
# to reach the target in the smallest dimension.
# Time - O(d**8) where d is the number of moves to reach the target.
# Space - O(d**8)

import heapq

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        def heuristic(cell):
            dx, dy = abs(cell[0] - x), abs(cell[1] - y)
            min_d, max_d = sorted([dx, dy])
            max_moves = (max_d + 1) // 2
            return max_moves + max(0, (min_d - max_moves + 1) // 2)

        queue = [[heuristic((0, 0)), 0, (0, 0)]]    # [min total moves possible, moves so far, cell]
        seen = set()

        while True:
            _, moves, cell = heapq.heappop(queue)
            if cell == (x, y):
                return moves

            if cell in seen:                        # ignore cells already reached
                continue
            seen.add(cell)

            for dx, dy in [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (-1, -2), (1, -2)]: # 8 moves
                new_cell = (cell[0] + dx, cell[1] + dy)
                if new_cell not in seen:
                    heapq.heappush(queue, [heuristic(new_cell) + moves + 1, moves + 1, new_cell])
