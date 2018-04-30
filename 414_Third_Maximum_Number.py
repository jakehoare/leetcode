_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/third-maximum-number/
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return
# the maximum number. The time complexity must be in O(n).

# Iterate over nums. If a number is already one of the top 3 largest unique numbers then ignore it. If larger than
# the largest, update largest and demote the first and second largest to second and third. Else if more than the
# second largest, replace second largest and demote previous second to third. Else if more than third, replace third.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxima = [float("-inf")] * 3    # maxima[0] is largest unique number seen, maxima[1] is second

        for num in nums:

            if num in maxima:
                continue

            if num > maxima[0]:
                maxima = [num] + maxima[:2]
            elif num > maxima[1]:
                maxima[1:] = [num, maxima[1]]
            elif num > maxima[2]:
                maxima[2] = num

        return maxima[2] if maxima[2] != float("-inf") else maxima[0]
