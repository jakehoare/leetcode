_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.

# Indicate that nums[i] has been seen by setting the i-1th entry to be negative.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for i in range(len(nums)):

            num = abs(nums[i])      # nums[i] may be negative because we have seen i + 1, which is irrelevant here

            if nums[num - 1] < 0:   # already seen num
                result.append(num)
                continue

            nums[num - 1] = -nums[num - 1]  # flag num as having been seen

        return result

