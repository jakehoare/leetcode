_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/duplicate-zeros/
# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written.
# Do the above modifications to the input array in place, do not return anything from your function.

# Iterate along arr, updating the new length after duplicating zeros.
# Find the index i in arr when the array with duplicates is full.
# Then iterate backwards from i, moving each element to its new index and duplicating zeros.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length = 0              # length of arr after duplicating zeros
        for i, num in enumerate(arr):
            length += 2 if num == 0 else 1
            if length >= len(arr):
                break

        next_fill = len(arr) - 1
        if length > len(arr):   # only one of the duplicate zero fits in arr
            arr[-1] = 0
            i -= 1
            next_fill -= 1

        for j in range(i, -1, -1):
            arr[next_fill] = arr[j]
            next_fill -= 1
            if arr[j] == 0:
                arr[next_fill] = arr[j]
                next_fill -= 1
