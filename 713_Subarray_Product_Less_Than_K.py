_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subarray-product-less-than-k/
# You are given an array of positive integers nums. Count and print the number of (contiguous) subarrays where the
# product of all the elements in the subarray is less than k.

# Maintain a window with product <= k. For each num, add to window product. While window contains some nums and
# product is too large, remove from window start. Increment result by window length since each subarray ending at end
# is valid. If start > end then product == 1.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subarrays = 0
        start = 0           # index of window start
        product = 1         # current product

        for end, num in enumerate(nums):

            product *= num

            while product >= k and start <= end:    # remove from window if product too large and window non-zero
                product //= nums[start]
                start += 1

            subarrays += end - start + 1            # if start = end + 1 then nothing added

        return subarrays