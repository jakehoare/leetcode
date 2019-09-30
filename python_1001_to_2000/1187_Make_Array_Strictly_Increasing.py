_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/make-array-strictly-increasing/
# Given two integer arrays arr1 and arr2,
# return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length
# and do the assignment arr1[i] = arr2[j].
# If there is no way to make arr1 strictly increasing, return -1.

# Maintain a mapping from the last num of the array so far and the number of operations to make this array.
# For each num of arr1, create a new mapping with default value of infinity.
# For each ending num of previous arrays,
#   If num > prev_num then we can make an array ending num with the same operations as made prev_num
#   Find the next number in arr2 greater than prev_num. if num <= prev_num then we can make an array ending in arr2[i]
#   with an extra operation. Similarly we can use the extra operation if num > prev_num only if arr2[i] < num (else we
#   are better extending with no additional operation).
# Time - O(n**2)
# Space - O(n)

from collections import defaultdict
import bisect

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr2.sort()
        num_to_ops = {-1: 0}  # map last number of array to number of ops to make array increasing

        for num in arr1:
            new_num_to_ops = defaultdict(lambda: float("inf"))

            for prev_num in num_to_ops:
                if num > prev_num:      # same nb ops to extend with num
                    new_num_to_ops[num] = min(new_num_to_ops[num], num_to_ops[prev_num])

                i = bisect.bisect_right(arr2, prev_num)
                if i < len(arr2) and (num <= prev_num or arr2[i] < num):
                    new_num_to_ops[arr2[i]] = min(new_num_to_ops[arr2[i]], num_to_ops[prev_num] + 1)

            num_to_ops = new_num_to_ops

        if num_to_ops:
            return min(num_to_ops.values())
        return -1
