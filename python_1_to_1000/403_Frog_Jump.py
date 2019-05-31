_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/frog-jump/
# A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone.
# The frog can jump on a stone, but it must not jump into the water.
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the
# river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.
# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units.
# Note that the frog can only jump in the forward direction.

# For each stone, create a set of previous jump distances that can reach that stone.
# For each jump size that can reach each stone, for each of the 3 jump sizes, if this reaches another stone add it
# to the set of jumps that can reach that next stone.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        jumps = {}  # key is stone position, value is set of jump sizes that can reach that stone
        for stone in stones:
            jumps[stone] = set()
        jumps[0].add(0)

        for stone in stones:
            for jump in jumps[stone]:
                for shift in [-1, 0, 1]:
                    if jump + shift > 0 and stone + jump + shift in jumps:
                        jumps[stone + jump + shift].add(jump + shift)

        return bool(jumps[stones[-1]])