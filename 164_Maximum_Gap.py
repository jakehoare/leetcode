_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-gap/
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
# Return 0 if the array contains less than 2 elements.
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

# Bucket sort.
# By pigeon-hole principle we ensure at least one bucket is empty (or all numbers in span are present).
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
        span = max(nums) - lower + 1
        if span < 2:                                # all same or 2 adjacent integers
            return span-1

        nb_buckets = min(span, len(nums) + 1)       # ensure an empty bucket with len(nums)+1, flooring width at 1
        width = span // nb_buckets                  # width of each bucket
        if span % nb_buckets != 0:                  # round up so all of span is covered
            width += 1
        buckets = [[None, None] for _ in range(nb_buckets)]     # min and max of nums in each bucket

        for num in nums:                            # update min and max of corresponding bucket
            bucket = (num - lower) // width
            buckets[bucket][0] = min(buckets[bucket][0], num) if buckets[bucket][0] else num
            buckets[bucket][1] = max(buckets[bucket][1], num) if buckets[bucket][1] else num

        last_used_bucket, max_gap = 0, 1            # default max gap to 1 if no gaps in buckets
        for i in range(len(buckets)-1):
            if not buckets[i][0] and buckets[i+1][0]:   # update max_gap if bucket is empty but next bucket is not
                max_gap = max(max_gap, buckets[i+1][0] - buckets[last_used_bucket][1])
            elif buckets[i][0]:
                last_used_bucket = i

        return max_gap
