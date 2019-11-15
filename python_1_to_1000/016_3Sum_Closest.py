_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/3sum-closest/
# Given an array nums of n integers, find three integers in nums such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Sort the array. For each staring index bidirectional search in the rest of the array.
# Time - O(n**2)
# Space - O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')  # default if len(nums) < 3

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:

                triple = nums[i] + nums[j] + nums[k]
                if triple == target:    # early return, cannot do better
                    return target
                if abs(triple - target) < abs(closest - target):
                    closest = triple

                if triple - target > 0:
                    k -= 1
                else:
                    j += 1

        return closest
