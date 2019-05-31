_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-city-scheduling/
# There are 2N people a company is planning to interview.
# The cost of flying the i-th person to city A is costs[i][0],
# and the cost of flying the i-th person to city B is costs[i][1].
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

# Sort the costs by the difference between flying to city A and city B.
# Fly the first half of the sorted list to city A and the second half to city B.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum(a for a, _ in costs[:n]) + sum(b for _, b in costs[n:])
