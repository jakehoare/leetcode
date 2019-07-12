_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-in-mountain-array/
# You may recall that an array A is a mountain array if and only if:
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
# If such an index doesn't exist, return -1.
# You can't access the mountain array directly.  You may only access the array using a MountainArray interface:
# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
# Also, any solutions that attempt to circumvent the judge will result in disqualification.

# Find the peak of the mountain by binary search.
# Binary search the left side of the peak, and if the target is not found then search the right side.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            next_val = mountain_arr.get(mid + 1)
            if next_val < val:      # slope down
                right = mid
            else:                   # slope up
                left = mid + 1

        mountain = left

        left, right = 0, mountain
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                right = mid - 1
            else:
                left = mid + 1

        left, right = mountain, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            if val > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
