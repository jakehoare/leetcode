_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subarray-sum-equals-k/
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose
# sum equals to k.

# Store counts of prefix sums in dictionary. Iterate over array, updating running_sum and incrementing result if
# running_sum == k. Lookup prefix value that makes a subararry of sum k.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        sums = defaultdict(int) # key is prefix sum, value is count of number of prefixes
        running_sum = 0

        for num in nums:

            running_sum += num

            if running_sum == k:
                total += 1
            if running_sum - k in sums:
                total += sums[running_sum - k]

            sums[running_sum] += 1

        return total