_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/contains-duplicate-iii/
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
# difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

# Map each num to a bucket of width t+1 so collision in bucket implies numbers are within t.  Also check
# higher and lower buckets.  Remove numbers from sliding window if more than k indices earlier.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0: # cannot have distinct integers if no index separation
            return False    # numerical separation must be positive
        buckets = {}        # map from a bucket to num in that bucket

        for i, num in enumerate(nums):
            bucket = num // (t + 1)     # bucket width t+1, collision implies difference <= t. handles t == 0
            if bucket in buckets:
                return True
            if bucket+1 in buckets and abs(num - buckets[bucket+1]) <= t:   # neighbouring buckets
                return True
            if bucket-1 in buckets and abs(num - buckets[bucket-1]) <= t:
                return True

            buckets[bucket] = num       # add to bucket
            if i - k >= 0:              # remove from start of window
                old_bucket = nums[i - k] // (t + 1)
                del buckets[old_bucket]

        return False