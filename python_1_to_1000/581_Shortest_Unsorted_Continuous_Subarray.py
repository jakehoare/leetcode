_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending
# order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.

# Iterate over nums from left to right. If any num is less than the previous then the previous must require sorting.
# Any number before the previous that is more than the minimum after the previous also requires sorting.
# Follow a similar procedure from right to left finding the first increase and subsequent maximum.
# Alternatively, compare a sorted copy of the list to the original list and find the first and last mismatches.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        right, left = -1, -1        # default values

        for i in range(1, n):
            if left == - 1 and nums[i] < nums[i - 1]:
                left = i - 1        # first index to be sorted
                min_num = nums[i]
            elif left != -1:        # update subsequent minimum
                min_num = min(min_num, nums[i])

        if left == -1:              # still default, list already sorted
            return 0

        for i in range(n - 2, -1, -1):
            if right == -1 and nums[i] > nums[i + 1]:
                right = i + 1       # last index to be sorted
                max_num = nums[i]
            elif right != -1:       # update subsequent maximum
                max_num = max(max_num, nums[i])

        while left > 0 and nums[left - 1] > min_num:        # nums[left - 1] requires sorting
            left -= 1
        while right < n - 1 and nums[right + 1] < max_num:  # nums[right + 1] requires sorting
            right += 1

        return right - left + 1