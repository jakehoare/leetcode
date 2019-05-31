_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Follow up for "153 Find Minimum in Rotated Sorted Array": What if duplicates are allowed?

# As per problem 153 except if nums[left] == nums[right] == nums[mid] must search both left and right.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left < right:

            if nums[left] < nums[right]:    # already sorted
                break

            mid = (left + right) // 2

            if nums[right] < nums[mid]:
                left = mid + 1      # discontinuity on RHS of mid
            elif nums[right] > nums[mid] or nums[left] > nums[mid]:
                right = mid         # discontinuity is mid or LHS
            else:                   # nums[right] == nums[mid] == nums[left]
                left += 1
                right -= 1

        return nums[left]