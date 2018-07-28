_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
# Given an integer array sorted in ascending order, write a function to search target in nums.
# If target exists, then return its index, otherwise return -1. However, the array size is unknown to you.
# You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the
# array at index k (0-indexed).
# You may assume all integers in the array are less than 10000, and if you access the array out of bounds,
# ArrayReader.get will return 2147483647.
# You may assume that all elements in the array are unique.
# The value of each element in the array will be in the range [-9999, 9999].

# Since the array contains unique numbers from -9999 to 9999, there are not more than 20000 numbers.
# Use 20000 as the upper-bound index in binary search.
# This works because the ArrayReader returns MAXINT for indices beyond the array, which is exactly the same as
# searching an array of 20000 elements where the last elements are MAXINT.
# Time - O(1), due to upper bound on size of array
# Space - O(1)

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 20000

        while left <= right:

            mid = (left + right) // 2

            val = reader.get(mid)
            if target == val:
                return mid
            if target > val:
                left = mid + 1
            else:
                right = mid - 1

        return -1