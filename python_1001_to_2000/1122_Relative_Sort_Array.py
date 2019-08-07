_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/relative-sort-array/
# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
# Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

# Count each element of arr1.
# Iterate over arr2. If an element is in arr1 then add all instances from r1 to the result and delete from the count.
# Sort all remaining elements from arr1 that not in arr2 and all their instances to the result in sorted order.
# Time - O(m)
# Space - O(m log m + n)

from collections import Counter

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        arr1_counts = Counter(arr1)
        result = []

        for val in arr2:
            if val in arr1_counts:
                result += [val] * arr1_counts[val]
                del arr1_counts[val]

        for val in sorted(arr1_counts.keys()):
            result += [val] * arr1_counts[val]

        return result
