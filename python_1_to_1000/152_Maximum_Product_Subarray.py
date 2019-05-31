_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-product-subarray/
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Calculate the most positive and most negative subarray products ending at each element.
# Either the element alone or multiplied by previous most positive or most negative.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_product = float('-inf')
        most_neg, most_pos = 1, 1

        for num in nums:
            most_pos, most_neg = max(num, most_pos * num, most_neg * num), min(num, most_pos * num, most_neg * num)
            largest_product = max(largest_product, most_pos, most_neg)

        return largest_product
