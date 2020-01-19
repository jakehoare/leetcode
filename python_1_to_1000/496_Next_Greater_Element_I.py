_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/next-greater-element-i/
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
# Find all the next greater numbers for nums1's elements in the corresponding places of nums2.
# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
# If it does not exist, output -1 for this number.

# Map the integers to be found to their indices in the result. Iterate over nums2, maintaining a stack of nums seen
# without a greater number, hence stack is descending. For each num, pop from stack all smaller nums and update the
# result if they are in nums1. Add each num to stack.
# Time - O(n) len(nums2)
# Space - O(m) len(nums1)

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [-1] * len(nums1)                      # default -1 if not overwritten

        find_to_i = {}                                  # key is num to be found, value is index
        for i, num in enumerate(nums1):
            find_to_i[num] = i

        stack = []
        for num in nums2:
            while stack and num > stack[-1]:            # num is first greater than top of stack
                smaller = stack.pop()
                if smaller in find_to_i:
                    result[find_to_i[smaller]] = num
            stack.append(num)

        return result 
