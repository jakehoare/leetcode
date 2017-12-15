_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rotate-array/
# Rotate an array of n elements to the right by k steps.

# Reverse entire array, then reverse left k elements and right n-k elements.
# Alternatively, split after n-k elements and swap slices.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

class Solution2(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]