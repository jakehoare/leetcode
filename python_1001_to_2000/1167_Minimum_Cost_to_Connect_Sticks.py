_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# You have some sticks with positive integer lengths.
# You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.
# You perform this action until there is one stick remaining.
# Return the minimum cost of connecting all the given sticks into one stick in this way.

# Since the cost is proportional to the lengths of sticks connected, we want to connect the shortest sticks.
# Maintain a heap and repeatedly connect the shortest 2 sticks, putting the connected stick back on the heap.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        cost = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            cost += x + y
            heapq.heappush(sticks, x + y)

        return cost
