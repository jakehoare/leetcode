_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/optimal-division/
# Given a list of positive integers, the adjacent integers will perform the float division.
# For example, [2,3,4] -> 2 / 3 / 4.
# However, you can add any number of parenthesis at any position to change the priority of operations. You should
# find out how to add parenthesis to get the maximum result, and return the corresponding expression in string format.
# Your expression should NOT contain redundant parenthesis.

# First number is always numerator, second number is always denominator. Subsequent numbers should all be in
# numerator (since all >= 1). This is achieved by bracketing all other numbers together.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(s) for s in nums]
        result = nums[0]

        if len(nums) == 1:
            return result
        if len(nums) == 2:
            return result + "/" + nums[1]

        return result + "/(" + "/".join(nums[1:]) + ")"

