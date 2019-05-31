_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# For example, given sorted array nums = [1,1,1,2,2,3],
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.

# Maintain a pointer to the next index to contain a result.  If a new number does not have 2 copies already
# in result then add it.
# Time - O(2)
# Space - O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        next = 2    # next index to be filled with result

        for index in range(2, len(nums)):

            if nums[index] != nums[next-2]:     # result does not contain 2 copies of this num
                nums[next] = nums[index]
                next += 1

        return min(next, len(nums))