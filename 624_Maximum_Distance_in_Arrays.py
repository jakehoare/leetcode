_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-distance-in-arrays/
# Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different
# arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be
# their absolute difference |a-b|. Your task is to find the maximum distance.

# For each array, update the max_dist using either the maximum from this array and the previous minimum from other
# arrays, or the minimum from this array and the previous maximum from other arrays. Then update the maximum and
# minimum. Only uses the fist and last integer from each array.
# Time - O(n) number of arrays
# Space - O(1)

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        low, high = arrays[0][0], arrays[0][-1]
        max_dist = 0

        for array in arrays[1:]:

            max_dist = max(max_dist, abs(array[-1] - low), abs(array[0] - high))
            low = min(low, array[0])
            high = max(high, array[-1])

        return max_dist