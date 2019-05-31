_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/knight-probability-in-chessboard/
# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves.
# The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
# A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal
# direction, then one square in an orthogonal direction.
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece
# would go off the chessboard) and moves there.
# The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the
# probability that the knight remains on the board after it has stopped moving.

# Base case for N == 0 is 100% probability of remaining on the board for all cells.
# For each additional remaining move, calculate a grid of probabilities of remaining on the board from each cell.
# The new probability from a cell is the sum of the probabilities from each of the 8 reachable cells given one fewer
# remaining move.
# Only consider the upper left quarter of the board, since the remainder is symmetrical.
# Time - O(K * N**2)
# Space - O(N**2)

class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        M = N // 2              # M is the side length of the upper quarter
        if N % 2 == 1:          # add central row and column if N is odd
            M += 1

        def convert(r1, c1):    # convert a cell to its symmetrical equivalent in the upper quarter
            if r1 >= M:
                r1 = N - 1 - r1
            if c1 >= M:
                c1 = N - 1 - c1
            return [r1, c1]

        probs = [[1 for _ in range(M)] for _ in range(M)]       # 100% probability of remaining for no more moves

        for _ in range(K):

            new_probs = [[0 for _ in range(M)] for _ in range(M)]

            for r1 in range(M):
                for c1 in range(M):
                    prob = 0
                    for dr in [2, 1, -1, -2]:                   # for each possible move
                        for dc in [3 - abs(dr), abs(dr) - 3]:

                            if 0 <= r1 + dr < N and 0 <= c1 + dc < N:   # ignore if outside the board
                                r2, c2 = convert(r1 + dr, c1 + dc)
                                prob += probs[r2][c2] / 8.0             # add 1/8 of probability

                    new_probs[r1][c1] = prob                    # update cell
            probs = new_probs                                   # update board

        r, c = convert(r, c)
        return probs[r][c]

