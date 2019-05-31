_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/intersection-of-two-arrays/
# Given two arrays, write a function to compute their intersection.

# Convert to sets, find intersection and convert back to list.
# Time - O(n + m)
# Space - O(n + m)

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))