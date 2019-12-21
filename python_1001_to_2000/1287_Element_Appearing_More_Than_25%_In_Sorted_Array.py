_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# Given an integer array sorted in non-decreasing order,
# there is exactly one integer in the array that occurs more than 25% of the time.
# Return that integer.

# Count the frequency of each num, returning the num when any count is more than 25%.
# Alternatively, for each num at 25%, 50% and 75% of the array, binary search for its first and last occurences.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        target = len(arr) // 4 + 1
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
            if counts[num] == target:
                return num
