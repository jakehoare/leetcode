_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/zuma-game/
# You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have
# several balls in your hand.
# Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and
# rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep
# doing this until no more balls can be removed. Find the minimal balls you have to insert to remove all the balls
# on the table. If you cannot remove all the balls, output -1.

# Iterate over board. When a sequence ends, if enough of same colour in hand to make a run of 3, add those balls
# from hand and recurse.
# Time - T(n) for board of length n = n**2 * T(n-3) since n recursions, each taking n time to remove_sequences
# then solving sub-problem of length n-3.

from collections import Counter

class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        def remove_sequences(board):    # recursively remove any sequences of length 3 or more
            start, end = 0, 0
            while end < len(board):
                if board[start] == board[end]:
                    end += 1
                elif end - start >= 3:
                    return remove_sequences(board[:start] + board[end:])
                else:
                    start = end
            if end - start >= 3:
                board = board[:start]
            return board

        def helper(board):
            if not board:
                return 0
            if not hand:
                return -1

            min_balls = 6           # since len(hand) <= 5
            start, end = 0, 0

            while end < len(board) + 1:

                if end == len(board) or board[start] != board[end]:
                    need = 3 - (end - start)    # number needed in hand to make a sequence of 3
                    colour = board[start]
                    if hand[colour] >= need:

                        hand[colour] -= need
                        next_board = remove_sequences(board[:start] + board[end:])
                        min_end = helper(next_board)
                        if min_end != -1:
                            min_balls = min(need + min_end, min_balls)
                        hand[colour] += need  # put balls back

                    start = end

                end += 1

            return -1 if min_balls == 6 else min_balls

        hand = Counter(hand)
        return helper(board)

