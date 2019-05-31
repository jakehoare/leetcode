_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given an array of integers that is already sorted in ascending order, find an ordered pair of indices of two numbers
# such that they add up to a specific target number.
# Please note that your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.

# Start pointers at both ends of array. Increment left if sum is too low or decrement right if sum is too high.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1

        while True:

            pair_sum = numbers[left] + numbers[right]
            if pair_sum == target:
                return [left+1, right+1]

            if pair_sum < target:
                left += 1
            else:
                right -= 1