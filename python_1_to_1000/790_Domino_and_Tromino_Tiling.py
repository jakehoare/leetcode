_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/domino-and-tromino-tiling/
# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.
# Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two
# 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

# For each length of board, find the number of tilings that fill the board exactly and the number of tilings that have
# one extra tile. To tile a board of length n exactly, we can use either a tiled board of n - 1 and a horizontal
# domino, or a tiled board of n - 2 and two vertical dominos, or a board of n - 2 with one extra tile and a tromino.
# To tile a board of length n with one extra tile, we can either use a fully tiled board of length n - 1 and a tromino
# in one of two orientations, or a a board of n - 2 with one extra tile and a vertical domino.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        prev_tilings, tilings = 0, 1        # one way to fully tile board of length zero
        prev_one_extra, one_extra = 0, 0    # no ways to tile boards of length -1 or 0 with one extra

        for _ in range(N):

            next_tilings = (tilings + prev_tilings + prev_one_extra) % MOD
            next_one_extra = (2 * tilings + one_extra) % MOD

            tilings, prev_tilings = next_tilings, tilings
            one_extra, prev_one_extra = next_one_extra, one_extra

        return tilings