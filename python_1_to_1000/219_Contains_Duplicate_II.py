_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/contains-duplicate-ii/
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Create a set of nums in a sliding window of length k. Iterate over nums, removing the num at the back of the window,
# checking if the new num is already in the window, or else adding it.
# Time - O(n)
# Space - O(k)

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()      # elements in window must be unique or else solution already found

        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])
            if num in window:
                return True
            window.add(num)

        return False
