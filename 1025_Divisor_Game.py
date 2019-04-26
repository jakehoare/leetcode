_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/divisor-game/
# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# Also, if a player cannot make a move, they lose the game.
# Return True if and only if Alice wins the game, assuming both players play optimally.

# If N is even, Alice can always subtract 1 and make N - x odd for Bob.
# If N is odd, then it only has odd factors so N - x will always be even or no move is possible if N == 1.
# Thus N will alternate between even and odd and the person with the even numbers will always be able to make a move.
# The person with odd numbers will eventually have 1 and lose.
# Time - O(1)
# Space - O(1)

class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
