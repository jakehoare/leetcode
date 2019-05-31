_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/4sum/
# Given an array nums of n integers, are there elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.

# Recursively reduce to 2sum problem.
# Time - O(n^3), for each pair perform linear search on the rest of the array

class Solution(object):
    ELEMENTS = 4        # parametrise the number of elements being summed

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        self.n_sum(sorted(nums), target, [], self.ELEMENTS, results)
        return results


    def n_sum(self, nums, target, partial, n, results):                 # generalise for n-sum

        if len(nums) < n or target > nums[-1]*n or target < nums[0]*n:  # early return if impossible
            return

        if n == 2:                      # base case of linear bidirectional search for n == 2
            left = 0
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(partial + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[right] == nums[right+1] and right > left:    # move to next different number if target found
                        right -=1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        else:
            for i in range(len(nums)-n+1):              # for all possible first numbers nums[i]
                if i == 0 or nums[i] != nums[i-1]:      # if not duplicate
                    self.n_sum(nums[i+1:], target-nums[i], partial + [nums[i]], n-1, results)
