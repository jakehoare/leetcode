_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
# which contains initial elements from the stream. For each call to the method KthLargest.add,
# return the element representing the kth largest element in the stream.

# Create a heap of nums and if there are more than k elements, pop off small elements until it has the k largest.
# If val cannot change kth largest, discard it and return kth largest. Else insert val, pop off an element if the
# heap is too big and return the kth largest.
# Time - O(n + (n - k)log n) for __init__ to heapify and pop off excess elements, O(log k) for add
# Space - O(k)

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) == self.k and val <= self.nums[0]:    # heap full and val does not chahnge kth largest
            return self.nums[0]

        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
