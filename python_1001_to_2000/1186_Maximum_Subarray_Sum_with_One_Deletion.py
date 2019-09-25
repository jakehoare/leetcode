_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
# Given an array of integers,
# return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion.
# In other words, you want to choose a subarray and optionally delete one element from it so that there is still
# at least one element left and the sum of the remaining elements is maximum possible.
# Note that the subarray needs to be non-empty after deleting one element.

# Iterate over the array, tracking the max sum ending at each index and the max sum ending at each index with one
# deletion.
# Max sum takes the previous max sum if positive or zero, and adds the current num.
# Max sum with deletion take the max sum and deletes the current num,
# or the previous max with deletion and adds the current num.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if all(a <= 0 for a in arr):    # no positive, return largest value
            return max(arr)

        overall_max_deleted = 0
        max_here, max_here_deleted = 0, 0

        for a in arr:
            max_here_deleted = max(max_here_deleted + a, max_here)
            max_here = max(max_here, 0) + a

            overall_max_deleted = max(overall_max_deleted, max_here_deleted, max_here)

        return overall_max_deleted
