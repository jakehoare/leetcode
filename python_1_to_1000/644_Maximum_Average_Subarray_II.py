_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-average-subarray-ii/
# Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k that
# has the maximum average value. And you need to output the maximum average value.

# If k is low (< 80) then calculate the cumulative sum array of nums and for each length find the average of all
# subarrays. Any subarray longer than 2k can be divided into 2 subarrays of length at least k, at one of which has an
# average at least as good as the whole subarray. Hence restrict to max length less than 2k.
# For larger k, binary search the space of averages. has_average(x) determines whether there is some subarray of
# length at least k with an average of at least x. Subtract x from all elements of nums, then for all prefixes of
# length at least k, find the minimum sum prefix that still allows subarray to be length k.
# Time - O(n log r) where r is range between max an min values of array. O(nk) for small k.
# Space - O(n) fro small k, O(1) for binary search.

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)

        if k < 80:
            cumulative = [0]
            for num in nums:
                cumulative.append(cumulative[-1] + num)
            result = float('-inf')
            for length in range(k, min(n + 1, 2 * k)):
                max_sum = max([cumulative[length + i] - cumulative[i] for i in range(n - length + 1)])
                result = max(result, max_sum / float(length))
            return result

        def has_average(x):

            subarray_sum = 0
            for i in range(k):
                subarray_sum += nums[i] - x
            if subarray_sum >= 0:
                return True

            prefix_sum, min_prefix = 0, 0
            for i in range(k, n):
                subarray_sum += nums[i] - x
                prefix_sum += nums[i - k] - x
                min_prefix = min(min_prefix, prefix_sum)
                if subarray_sum - min_prefix >= 0:
                    return True

            return False

        left, right = min(nums), max(nums)
        while right - left > 1e-5:
            mid = (left + right) / 2.0
            if has_average(mid):
                left = mid
            else:
                right = mid

        return left