_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/patching-array/
# Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number
# in range [1, n] inclusive can be formed by the sum of some elements in the array.
# Return the minimum number of patches required.

# At each stage we add the lowest missing number to the sequence.  If the next num is <= next_missing then it can
# be used to extend the sequence without a patch.  Or else we patch with next_missing, which extends the sequence
# as far as possible.
# Time - O(m + log n) where m = len(nums)
# Space - O(1)

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        next_missing = 1
        patches = 0
        i = 0

        while next_missing <= n:
            if i < len(nums) and nums[i] <= next_missing:
                next_missing += nums[i]
                i += 1
            else:
                next_missing += next_missing
                patches += 1

        return patches
