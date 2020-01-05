_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
# Given an array arr,
# replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.

# Iterate over the array from right to left.
# Simultaneously update the greatest value seen and replace the value with the greatest.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        greatest = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], greatest = greatest, max(greatest, arr[i])

        return arr
