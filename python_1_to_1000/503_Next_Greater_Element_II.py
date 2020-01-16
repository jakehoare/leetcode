_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/next-greater-element-ii/
# Given a circular array (the next element of the last element is the first element of the array), print the Next
# Greater Number for every element. The Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly to find its next greater number.
# If it doesn't exist, output -1 for this number.

# Stack holds indices of numbers without greater element, hence decreasing order. Pop of all numbers lower than
# current and set their next_greater to current. Repeat iteration over nums to account for circularity.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = []                          # indices whose nums form decreasing sequence
        next_greater = [-1] * n             # default -1 if no greater

        for i in range(2 * n):
            num = nums[i % n]               # wrap around
            while stack and num > nums[stack[-1]]:
                next_greater[stack.pop()] = num
            if i < n:
                stack.append(i)

        return next_greater
