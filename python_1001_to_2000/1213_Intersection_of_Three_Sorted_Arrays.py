_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/intersection-of-three-sorted-arrays/
# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
# return a sorted array of only the integers that appeared in all three arrays.

# Count the frequency across all arrays.
# Return the items that occur 3 times.
# This works because the arrays are strictly increasing, i.e. no duplicates.
# Also works if the arrays are not sorted.
# Time - O(n)
# Space - O(n)

from collections import Counter

class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        return [i for i, count in Counter(arr1 + arr2 + arr3).items() if count == 3]
