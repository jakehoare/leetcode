_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/3sum-smaller/
# Given an array of n integers nums and a target, find the number of index triplets i, j, k
# with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target

# Sort the array.  For each index i search nums[i+1, len(nums)].  Whenever a triple sums to less than target we
# increment the count by right - left since for that value of the left pointer all values to the left of nums[right]
# also form a triplet less than the target.
# Time - O(n**2)
# Space - O(1)

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()

        for i in range(len(nums)-2):

            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count