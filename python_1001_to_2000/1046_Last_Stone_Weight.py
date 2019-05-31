_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/last-stone-weight/
# We have a collection of rocks, each rock has a positive integer weight.
# Each turn, we choose the two heaviest rocks and smash them together.
# Suppose the stones have weights x and y with x <= y.
# The result of this smash is:
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Create a heap of the stones. While the are at least 2 stones, pop off the largest 2 weights and smash them.
# Add the resulting stone back to the heap if it has non-zero weight.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-stone for stone in stones]           # negative so largest values are popped first
        heapq.heapify(stones)

        while len(stones) > 1:
            new = heapq.heappop(stones) - heapq.heappop(stones)
            if new != 0:
                heapq.heappush(stones, new)

        return -stones[0] if stones else 0
