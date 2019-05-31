_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-mountain-array/
# Given an array A of integers, return true if and only if it is a valid mountain array.
# Recall that A is a mountain array if and only if:
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]

# Increment left pointer as long as array is increasing. Decrement right pointer as long as array is decreasing.
# Pointers must meet and not be at ends.
# Time - O(n)
# Space - O(1)

class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n = len(A)
        left, right = 0, n - 1

        while left + 1 < n - 1 and A[left + 1] > A[left]:
            left += 1
        while right - 1 > 0 and A[right - 1] > A[right]:
            right -= 1

        return 0 < left == right < n - 1