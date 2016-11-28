_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in
# the sorted order, not the kth distinct element.

# Quick select. Partition array about random element.  Narrow search region to one side of partition.
# Time - O(n), recurse on half (random) of array
# Space - O(1)

import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k               # find index k when sorted ascendingly
        left, right = 0, len(nums)-1
        while True:
            index = self.partition(nums, left, right)   # all entries < index are <= nums[index]
            if index == k:
                return nums[index]
            if index > k:
                right = index-1
            else:
                left = index+1


    def partition(self, nums, left, right):

        rand_index = random.randint(left, right)
        rand_entry = nums[rand_index]
        nums[rand_index], nums[right] = nums[right], nums[rand_index]   # swap rand_index to right

        next_lower = left       # the next index there an entry <= rand_entry will be stored
        for i in range(left, right):
            if nums[i] <= rand_entry:   # no action if > rand_entry
                nums[next_lower], nums[i] = nums[i], nums[next_lower]
                next_lower += 1

        nums[next_lower], nums[right] = nums[right], nums[next_lower]   # swap rand_entry back to be next_lower
        return next_lower
