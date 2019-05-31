_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/snakes-and-ladders/
# On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the
# board, and alternating direction each row.
# You start on square 1 of the board (which is always in the last row and first column).
# Each move, starting from square x, consists of the following:
# You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
# (This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations.)
# If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
# A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.
# The destination of that snake or ladder is board[r][c].
# Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the
# start of another snake or ladder, you do not continue moving.
# For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you
# finish your first move at `3`, because you do not continue moving to `4`.
# Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

# Breadth-first search. First convert the board to a 1-dimensional list of the squares in order.
# Queue contains all current indices. In each cycle of the while loop, for each index move up or down any ladder
# or snake, then take from 1 to 6 steps.
# Time - O(n**2)
# Space - O(n**2)

class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        linear = [-1]               # convert board to a list (deboustrophedonization)
        reverse = False             # alternate rows are appended not reversed and reversed

        for row in board[::-1]:     # start from last row
            linear += row[::-1] if reverse else row
            reverse = not reverse

        moves = 0
        visited = set()             # indices (before any snake or ladder)
        queue = {1}                 # board moves are indexed from 1

        while queue:

            new_queue = set()

            for i in queue:

                if i in visited or i >= len(linear):    # ignore positions seen already or too far
                    continue
                visited.add(i)

                if linear[i] != -1:                     # snake or ladder
                    i = linear[i]
                if i == len(linear) - 1:
                    return moves

                for step in range(1, 7):                # take 1 to 6 steps
                    new_queue.add(i + step)

            moves += 1
            visited |= queue
            queue = new_queue

        return -1
