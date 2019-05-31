_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/min-cost-climbing-stairs/
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of
# the floor, and you can either start from the step with index 0, or the step with index 1.

# Dynamic programming. Track the cost of reaching each step and the previous step. The cost of reaching any step is
# the cost of that step plus the lower cost of reaching the precious 2 steps.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev, step = cost[:2]

        for c in cost[2:]:
            prev, step = step, c + min(prev, step)

        return min(prev, step)      # finish at last or penultimate step