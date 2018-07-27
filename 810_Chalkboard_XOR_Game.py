_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/chalkboard-xor-game/
# We are given non-negative integers nums[i] which are written on a chalkboard.
# Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.
# If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.
# Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.
# Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0,
# then that player wins.
# Return True if and only if Alice wins the game, assuming both players play optimally.

# If there are an even number of nums and xor is not zero, then there are at least 2 different nums. Alice can always
# remove a number not equal to the xor of all numbers, so the xor will not be zero.
# Time - O(n)
# Space - O(1)

from functools import reduce
import operator

class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return reduce(operator.xor, nums) == 0 or len(nums) % 2 == 0