_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/increasing-triplet-subsequence/
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Track the smallest num seen so far and the next_smallest.  If we see a num larger than next_smallest, return True.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallest, next_smallest = float("inf"), float("inf")

        for num in nums:
            smallest = min(smallest, num)
            if num > smallest:
                next_smallest = min(next_smallest, num)
            if num > next_smallest:
                return True

        return False