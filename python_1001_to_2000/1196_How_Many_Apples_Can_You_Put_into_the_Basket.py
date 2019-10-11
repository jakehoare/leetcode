_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/
# You have some apples, where arr[i] is the weight of the i-th apple.
# You also have a basket that can carry up to 5000 units of weight.
# Return the maximum number of apples you can put in the basket.

# Form a heap of the apples.
# Remove apples from the heap by increasing weight,
# until there are no more apples or there is insufficient capacity to fit the next apple in the basket.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        capacity = 5000
        apples = 0
        heapq.heapify(arr)
        while arr and capacity - arr[0] >= 0:
            capacity -= heapq.heappop(arr)
            apples += 1

        return apples
