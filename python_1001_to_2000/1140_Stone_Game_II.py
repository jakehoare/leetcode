_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/stone-game-ii/
# Alex and Lee continue their games with piles of stones.
# There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones.
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first X remaining piles,
# where 1 <= X <= 2M. Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

# Convert the array so piles[i] is the sum of all remaining piles.
# Recursive helper function calculates the result from pile i for a given value of M.
# Return the best result for each value of x of taking the remaining piles minus the best case for the next player.
# Memoize to avoid repetition.
# Time - O(n**3) since there are O(n**2) states, each taking O(n) to compute.
# Space - O(n**2)

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]    # convert to cumulative sum from end
        memo = {}

        def helper(i, M):
            if i + 2 * M >= n:          # take all remaining piles
                return piles[i]
            if (i, M) in memo:
                return memo[(i, M)]

            best = 0
            for x in range(1, 2 * M + 1):   # try all valid values of x
                best = max(best, piles[i] - helper(i + x, max(M, x)))

            memo[(i, M)] = best
            return best

        return helper(0, 1)
