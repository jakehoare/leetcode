_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/target-sum/
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -.
# For each integer, you should choose one from + and - as its new symbol.
# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Keep count of frequency of all possible sums that could reach target in dictionary. For each num, increment and
# decreement all sums, removing those that cannot reach target.
# Time - O(2**(n+1))
# Space - O(2**n)

from collections import defaultdict


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = defaultdict(int)
        sums[0] = 1
        running = nums[:]       # calc remaining sum from each index

        for i in range(len(nums) - 2, -1, -1):
            running[i] += running[i + 1]

        for i, num in enumerate(nums):

            new_sums = defaultdict(int)
            for old_sum in sums:
                if S <= old_sum + running[i]:   # add to neew_sums if not too large
                    new_sums[old_sum + num] += sums[old_sum]
                if S >= old_sum - running[i]:
                    new_sums[old_sum - num] += sums[old_sum]
            sums = new_sums

        if S not in sums:
            return 0
        return sums[S]