_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-number-of-nice-subarrays/
# Given an array of integers nums and an integer k.
# A subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Find the indices of odd numbers.
# For each block of consecutive k indices, find the number of even indices before and after this block.
# Multiple the even indices before and after, since for each starting index we can construct a valid subarray with
# any odd index.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        odds = [-1] + [i for i, num in enumerate(nums) if num % 2 == 1] + [len(nums)]
        result = 0

        for j, end in enumerate(odds[k:-1], k):         # ending indices of each consecutive k odd numbers
            ends = odds[j + 1] - end                    # array can end from end to (excluding) next odd
            starts = odds[j - k + 1] - odds[j - k]
            result += starts * ends
        return result
