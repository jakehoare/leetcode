_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-valid-subarrays/
# Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following:
# The leftmost element of the subarray is not larger than other elements in the subarray.

# Maintain a stack of leftmost elements in increasing order.
# Iterate along nums, popping from the stack all leftmost elements that are greater than the current element.
# Add the current element and increment the result by the count of leftmost elements on the stack.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        stack = []  # leftmost elements

        for num in nums:

            while stack and stack[-1] > num:    # remove elements from stack
                stack.pop()
            stack.append(num)

            result += len(stack)

        return result
