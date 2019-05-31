_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/moving-stones-until-consecutive/
# Three stones are on a number line at positions a, b, and c.
# Each turn, you pick up a stone at an endpoint (ie., either the lowest or highest position stone),
# and move it to an unoccupied position between those endpoints.
# Formally, let's say the stones are currently at positions x, y, z with x < y < z.
# You pick up the stone at either position x or position z, and move that stone to an integer position k,
# with x < k < z and k != y.
# The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.
# When the game ends, what is the minimum and maximum number of moves that you could have made?
# Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

# Sort the stones and calculate the length of the 2 gaps between stones.
# If either gap is 1 then the minimum moves if 1 since a stone can fill the gap. Else move each outer stone next to
# the middle stone if there is a gap.
# The maximum number of moves happens when the outer stones are moved in 1 place every turn.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        stones = sorted([a, b, c])
        gap1, gap2 = stones[1] - stones[0] - 1, stones[2] - stones[1] - 1
        min_moves = 1 if gap1 == 1 or gap2 == 1 else int(gap1 > 0) + int(gap2 > 0)
        max_moves = gap1 + gap2
        return [min_moves, max_moves]
