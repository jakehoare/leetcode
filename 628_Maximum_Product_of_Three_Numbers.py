_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-product-of-three-numbers/
# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# For 2 numbers, maximum is either largest pair or smallest (most negative) pair.
# For 3 numbers, use the maximum from 2 numbers and the next largest.
# Sort the array to find the smallest and largest, alternatively iterate over array tracking top 3 and bottom 2 in O(n).
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        top_3 = nums[-1] * nums[-2] * nums[-3]
        top_bottom = nums[-1] * nums[0] * nums[1]

        return max(top_3, top_bottom)

