_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
# Given an integer array arr and a target value target,
# return the integer value such that when we change all the integers larger than value
# in the given array to be equal to value,
# the sum of the array gets as close as possible (in absolute difference) to target.
# In case of a tie, return the minimum such integer.
# Notice that the answer is not necessarily a number from arr.

# Binary search for the first integer ceiling that makes the array sum >= target.
# Then check if integer - 1 ceiling can make the array sum closer to the target.
# Time - O(n log k) where k is the range of values in arr
# Space - O(1)

class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, max(arr)

        def ceiling(x):
            return sum(min(a, x) for a in arr)

        while low < high:
            mid = (low + high) // 2
            value = ceiling(mid) - target
            if value >= 0:
                high = mid
            else:
                low = mid + 1

        value = ceiling(low) - target
        lower = ceiling(low - 1) - target
        return low - 1 if abs(lower) <= abs(value) else low     # return low - 1 if closer or same diff to target
