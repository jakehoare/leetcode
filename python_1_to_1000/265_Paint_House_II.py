_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/paint-house-ii/
# There are a row of n houses, each house can be painted with one of the k colors.
# The cost of painting each house with a certain color is different. You have to paint all the houses such that
# no two adjacent houses have the same color.

# For each house, calculate the min cost of painting that house each colour given min costs of painting upto the
# previous house each colour.
# Find the colour that minimises the cost of painting upto and including the previous house.  The min cost of painting
# the next house any colour apart from the previous min cost colour is the cost of the previous min cost + new colour.
# The min cost of painting the next house the same as the previous min colour is the cost of painting previous house
# is second lowest cost colout + new colour.
# Time - O(nk)
# Space - O(1)

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0

        for i in range(1, len(costs)):

            min_colours = [0, 1]    # colours of previous house that give min and second min costs
            if costs[i-1][0] > costs[i-1][1]:
                min_colours = [1, 0]

            for colour in range(2, len(costs[0])):
                if costs[i-1][colour] <= costs[i-1][min_colours[0]]:    # new min cost
                    min_colours[1], min_colours[0] = min_colours[0], colour
                elif costs[i-1][colour] < costs[i-1][min_colours[1]]:   # new second min cost
                    min_colours[1] = colour

            for colour in range(len(costs[0])): # colour == min_colours[0] is 1 if colour is the min_colours[0]
                costs[i][colour] += costs[i-1][min_colours[colour == min_colours[0]]]

        return min(costs[-1])


