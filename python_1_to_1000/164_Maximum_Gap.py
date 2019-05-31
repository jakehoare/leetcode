_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-gap/
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
# Return 0 if the array contains less than 2 elements.
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

# Bucket sort. By pigeon-hole principle we ensure at least one bucket is empty or numbers are equally separated
# by the same distance.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        lower = min(nums)
        difference = max(nums) - lower
        gaps = len(nums) - 1        # number of spaces between sorted nums
        if difference == 0:         # all nums are same
            return 0

        width = difference // gaps  # range of integers // number of gaps
        if width == 0:
            width = 1

        nb_buckets = 1 + difference // width    # ensure max(nums) goes in final bucket

        buckets = [[None, None] for _ in range(nb_buckets)] # max and min of each bucket

        for num in nums:
            bucket = (num - lower) // width
            buckets[bucket][0] = min(buckets[bucket][0], num) if buckets[bucket][0] != None else num
            buckets[bucket][1] = max(buckets[bucket][1], num) if buckets[bucket][1] != None else num

        last_used_bucket = 0
        max_gap = difference // gaps  # default case of no empty buckets
        for i in range(nb_buckets - 1):
            if not buckets[i][0] and buckets[i + 1][0]:
                max_gap = max(max_gap, buckets[i + 1][0] - buckets[last_used_bucket][1])
            elif buckets[i][0]:
                last_used_bucket = i

        return max_gap
