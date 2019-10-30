_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/play-with-chips/
# There are some chips, and the i-th chip is at position chips[i].
# You can perform any of the two following types of moves any number of times (possibly zero) on any chip:
# Move the i-th chip by 2 units to the left or to the right with a cost of 0.
# Move the i-th chip by 1 unit to the left or to the right with a cost of 1.
# There can be two or more chips at the same position initially.
# Return the minimum cost needed to move all the chips to the same position (any position).

# Count the number of chips at odd and even positions.
# All chips within each group can be moved to the same position at no cost.
# Move the smaller group to the larger group, costing the size of the smaller group.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        evens, odds = 0, 0
        for chip in chips:
            if chip % 2 == 0:
                evens += 1
            else:
                odds += 1

        return min(evens, odds)
