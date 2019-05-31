_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/product-of-array-except-self/
# Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the
# product of all the elements of nums except nums[i].

# Iterate from left to right, calculating the product of all numbers to the left.
# The iterate from right to left, multiplying each result by the product of all numbers to the right.
# If any one value is zero then result is all zeros apart from that entry.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1]  # product of all to left of nums[0] is set to 1
        for i in range(1, len(nums)):
            products.append(nums[i-1] * products[-1])

        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]

        return products