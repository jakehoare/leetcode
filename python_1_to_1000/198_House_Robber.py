_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/house-robber/
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
# of money you can rob tonight without alerting the police.

# Either do not rob current house and take max from all previous houses, or rob current house, skip previous and
# take max of all others.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        loot, prev = nums[0], 0     # max from robbing this and previous adjacent houses

        for num in nums[1:]:
            loot, prev = max(num + prev, loot), loot

        return loot