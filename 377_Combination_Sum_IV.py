_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/combination-sum-iv/
# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that
# add up to a positive integer target.

# Top-down nb ways to make k for any num in nums is 1 if num == k, 0 if num > k, recurse if num < k.
# Alternatively, bottom up dynamic programming.
# Time - O(k) where k = target
# Space - O(k * n) where n = len(nums)

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        self.helper(nums, target, memo)
        return memo[target]

    def helper(self, nums, target, memo):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if target in memo:
            return memo[target]

        combos = 0
        for num in nums:
            combos += self.helper(nums, target - num, memo)
        memo[target] = combos
        return combos


class Solution2(object):
    def combinationSum4(self, nums, target):
        combos = [0] * (target + 1)  # combos[i] is nb ways wo make i
        combos[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    combos[i] += combos[i - num]

        return combos[-1]
