_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-subarray/
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For each num calculate the max subarray sum ending with that num as either num alone (if previous sum was -ve) or
# num + previous sum (if previous sum was +ve)
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall_max = float('-inf')
        max_ending_here = 0

        for num in nums:
            if max_ending_here > 0:
                max_ending_here += num
            else:
                max_ending_here = num
            overall_max = max(overall_max, max_ending_here)

        return overall_max