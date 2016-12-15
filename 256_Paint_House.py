_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/paint-house/
# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
# The cost of painting each house with a certain color is different. You have to paint all the houses such that no
# two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
# Find the minimum cost to paint all houses. All costs are positive integers.

# Min cost of painting a house any colour is the cost of painting that house that colour + min of painting the previous
# house a different colour.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])

        return min(costs[-1])