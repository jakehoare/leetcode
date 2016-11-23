_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element appears more than [n/2] times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# In order for an element to be a majority element of the array it must also be the majority element of some
# subarray.  Iterate over array creating subarrays assuming first element is majority.  Extend subarray to left, if
# candidate is no longer in the majority then start a new subarray.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, start, candidate = 0, 0, None

        for i, num in enumerate(nums):
            if not candidate:       # start new subarray with first element as candidate
                candidate = num
            if candidate == num:    # increment count
                count += 1
            if count <= (i - start + 1) // 2:   # candidate is no longer in the majority
                candidate = None

        return candidate        # majority always exists so do not need to check candidate is majority of whole array