_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Let's call an array A a mountain if the following properties hold:
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that
# A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

# Binary search for the first index where the number at the next element is lower.
# Time - O(log n)
# Space - O(l)

class Solution(object):
    def peakIndexInMountainArray(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 2

        while left < right:

            mid = (left + right) // 2

            if nums[mid + 1] < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left