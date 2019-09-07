_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/online-majority-element-in-subarray/
# Implementing the class MajorityChecker, which has the following API:
# MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the given array arr;
# int query(int left, int right, int threshold) has arguments such that:
# 0 <= left <= right < arr.length representing a subarray of arr;
# 2 * threshold > right - left + 1, ie. the threshold is always a strict majority of the length of the subarray
# Each query(...) returns the element in arr[left], arr[left+1], ..., arr[right]
# that occurs at least threshold times, or -1 if no such element exists.

# Create a map from each val of arr to an ordered list of indices with that val.
# Create a list of unique vals, in descending order of number of occurrences in arr.
# To query, start with the the num with the most indices and binary search for the left and right indices.
# Repeat with the next num, until a result or the num has fewer than threshold indices in arr.
# Time - O(n log n) for __init__ and O(n log n) for query.
# Space - O(n)

from collections import defaultdict
import bisect

class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.val_to_indices = defaultdict(list)
        for i, val in enumerate(arr):
            self.val_to_indices[val].append(i)

        self.vals = sorted(self.val_to_indices.keys(), key=lambda x: len(self.val_to_indices[x]), reverse=True)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for val in self.vals:
            if len(self.val_to_indices[val]) < threshold:
                break
            left_i = bisect.bisect_left(self.val_to_indices[val], left)
            right_i = bisect.bisect_right(self.val_to_indices[val], right)
            if right_i - left_i >= threshold:
                return val

        return -1
