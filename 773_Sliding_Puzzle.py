_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sliding-puzzle/
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
# Given a puzzle board, return the least number of moves required so that the state of the board is solved.
# If it is impossible for the state of the board to be solved, return -1.

# Breadth-first search. Expand queue from board by moving to all board positions after making a swap.
# Alternatively, A* search with heap and heuristic of manhattan distance between each tile and its target location.
# Time - O(mn * mn!) since there are mn! possible boards
# Space - O(mn * mn!)

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        nbors = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]  # indices of neighbouring cells in linear board

        def next_boards(b):                 # return list of next possible boards

            i = b.index(0)
            next_bds = []

            for nbor in nbors[i]:
                b_copy = b[:]               # make a copy
                b_copy[i], b_copy[nbor] = b_copy[nbor], b_copy[i]   # swap zero with neighbour
                next_bds.append(b_copy)
            return next_bds

        queue = [board[0] + board[1]]       # convert board to linear board
        steps = 0
        seen = set()                        # visited linear boards, as tuples

        while queue:

            new_queue = []

            for bd in queue:
                if bd == [1, 2, 3, 4, 5, 0]:
                    return steps
                seen.add(tuple(bd))
                new_queue += [nb for nb in next_boards(bd) if tuple(nb) not in seen]

            steps += 1
            queue = new_queue

        return -1
