_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
# Return the result as a list of indices representing the starting position of each interval (0-indexed).
# If there are multiple answers, return the lexicographically smallest one.

# Initialise one, tow and three as the first three contiguous subarrays of length k in nums. Iterate over nums,
# moving the current 3 subarrays forward on every step. Update the best sum first subarray if greater. Update the best
# sum first 2 subarrays if the new second subarray plus the best first is greater. Update the best all 3 subarrays if
# the new third subarray plus the best first two sum is greater.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        one_sum = sum(nums[:k])                 # sums of current subarrays
        two_sum = sum(nums[k:k * 2])
        three_sum = sum(nums[k * 2:k * 3])

        best_one = one_sum                      # best sums of one, two and three subarrays
        best_two = one_sum + two_sum
        best_three = one_sum + two_sum + three_sum

        best_one_i = 0                          # start indices of best one, two and three subarrays
        best_two_i = [0, k]
        best_three_i = [0, k, k * 2]

        one_i = 1                               # next array start index
        two_i = k + 1
        three_i = k * 2 + 1

        while three_i <= len(nums) - k:

            one_sum += nums[one_i + k - 1] - nums[one_i - 1]    # update current subarray sums
            two_sum += nums[two_i + k - 1] - nums[two_i - 1]
            three_sum += nums[three_i + k - 1] - nums[three_i - 1]

            if one_sum > best_one:                  # one_sum in an improvement
                best_one = one_sum
                best_one_i = one_i

            if best_one + two_sum > best_two:       # two_sum and best_one are an improvement
                best_two = best_one + two_sum
                best_two_i = [best_one_i, two_i]

            if best_two + three_sum > best_three:   # three_sum and best_two are an improvement
                best_three = best_two + three_sum
                best_three_i = best_two_i + [three_i]

            one_i += 1
            two_i += 1
            three_i += 1

        return best_three_i