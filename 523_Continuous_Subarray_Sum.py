_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/continuous-subarray-sum/
# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous
# subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

# Subarray is difference between prefix sums a and b. a - b = nk. (a - b) % k = 0 hence a%k - b%k = 0.
# Store prefix sums % k in dictionary.
# prefix sums % k is zero.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_sum, prefix_sums = 0, {0: -1}  # key is prefix sum mod k, value is index in nums

        for i, n in enumerate(nums):

            prefix_sum += n
            if k != 0:  # if k == 0 then look for prefix sum difference of zero
                prefix_sum = prefix_sum % k

            if prefix_sum in prefix_sums:
                if i - prefix_sums[prefix_sum] > 1:     # check length >= 2
                    return True
            else:
                prefix_sums[prefix_sum] = i  # do not overwrite if key present already

        return False