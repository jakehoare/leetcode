_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two arrays, write a function to compute their intersection.
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.

# Count frequencies of nums in nums1. Iterate over nums2, for every num in nums1 with a positive count, append to
# result and decrement count in nums1.
# Time - O(m + n)
# Space - O(m)

from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq1 = Counter(nums1)

        result = []
        for i, num in enumerate(nums2):
            if num in freq1 and freq1[num] > 0:
                freq1[num] -= 1
                result.append(num)

        return result