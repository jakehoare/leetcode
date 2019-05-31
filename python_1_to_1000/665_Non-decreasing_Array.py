_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/non-decreasing-array/
# Given an array with n integers, check if it could become non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

# If an element is less than the previous element, if we have already modified the array then return False. Else we can
# either decrease the previous element or increase the current element. Decreasing the previous is preferred
# because it does not have an affect on future elements but is only possible if there is no element before previous
# or it is not more than the previous element. There is no need to actually modify the previous element since it is
# never used again.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified = False

        for i, num in enumerate(nums[1:], 1):

            if num < nums[i - 1]:

                if modified:
                    return False

                if i != 1 and nums[i - 2] > nums[i]:    # must increase nums[i]
                    nums[i] = nums[i - 1]

                modified = True

        return True

