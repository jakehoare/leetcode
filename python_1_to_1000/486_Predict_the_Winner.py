_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/predict-the-winner/
# Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the
# array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not
# be available for the next player. This continues until all the scores have been chosen.
# The player with the maximum score wins. If the scores of both players are equal, then player 1 is still the winner.
# Given an array of scores, predict whether player 1 is the winner. You can assume each player maximizes his score.

# Recursively remove left and right. For each case, find score after worst case next opponent move. Take best score of
# each case. Memoize.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def helper(left, right):

            if right < left:            # base case
                return 0
            if right == left:           # base case
                return nums[left]
            if (left, right) in memo:
                return memo[(left, right)]

            left_right = helper(left + 1, right - 1)
            left_left = helper(left + 2, right)
            take_left = nums[left] + min(left_right - nums[right], left_left - nums[left + 1])

            right_right = helper(left, right - 2)       # reuse left_right
            take_right = nums[right] + min(left_right - nums[left], right_right - nums[right - 1])

            result = max(take_left, take_right)
            memo[(left, right)] = result
            return result

        memo = {}
        return helper(0, len(nums) - 1) >= 0
