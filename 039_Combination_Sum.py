_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/combination-sum/
# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Subtract each candidate from target as many times as possible whilst remainder is non-negative. Recurse
# each time, moving on to the next candidate.
# Time - approx f^n where f is target/average_candidate and n is the number of candidates with this nb recursions

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(candidates, 0, target, [], result)
        return result

    def helper(self, nums, next, target, partial, result):
        if target == 0:
            result.append(partial)
            return
        if next == len(nums):
            return

        i = 0
        while target-i*nums[next] >= 0:
            self.helper(nums, next+1, target-i*nums[next], partial + [nums[next]]*i, result)
            i += 1
