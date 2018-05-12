_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.

# Iterate over the list. For every number seen, set the number with index of num - 1 to be negative.
# Iterate again over the list, finding all indices that are still positive and so have not been seen.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            num = abs(num)                          # may be negative so take absolute value
            nums[num - 1] = -abs(nums[num - 1])     # set nums[num - 1] to indicate num - 1 seen

        return [i + 1 for i, num in enumerate(nums) if num > 0]
