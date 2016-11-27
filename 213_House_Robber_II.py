_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/house-robber-ii/
# This is an extension of 198 House Robber.
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he
# will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first
# house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for
# those in the previous street.
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum
# amount of money you can rob tonight without alerting the police.

# As per 198 except consider the greater of 2 cases - allow robbing the first house but no the last, allow robbing the
# last house but not the first.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return sum(nums)    # 1 house has no neighbours

        loot, prev = 0, 0
        for num in nums[1:]:    # do not rob first house
            loot, prev = max(num + prev, loot), loot

        nums[-1] = 0            # do not rob last house
        loot2, prev = 0, 0
        for num in nums:
            loot2, prev = max(num + prev, loot2), loot2

        return max(loot, loot2)