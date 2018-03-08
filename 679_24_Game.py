_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/24-game/
# You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated
# through *, /, +, -, (, ) to get the value of 24.

# For any input list, iterate through every pair of numbers and combine them in all 6 possible ways. There are 6 ways
# because addition and multiplication are commutative but subtraction and division are not. Form a new shorter list
# from the result of the operation oin the pair and remaining unused numbers from the original list and recurse.
# The base case is a list with one element. Numerical precision implies this may not be exactly 24 but the minimum
# number that can eb formed is 1 / (9 * 9 * 9) and sets a bound on the tolerance.
# Time - O(1) since here are a finite number of combinations.
# Space - O(1)

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) < 0.001

        for i in range(n - 1):
            for j in range(i + 1, n):
                remainder = nums[:i] + nums[i + 1:j] + nums[j + 1:]

                if self.judgePoint24(remainder + [nums[i] + nums[j]]):
                    return True
                if self.judgePoint24(remainder + [nums[i] - nums[j]]):
                    return True
                if self.judgePoint24(remainder + [nums[j] - nums[i]]):
                    return True
                if self.judgePoint24(remainder + [nums[i] * nums[j]]):
                    return True
                if nums[j] != 0 and self.judgePoint24(remainder + [float(nums[i]) / float(nums[j])]):
                    return True
                if nums[i] != 0 and self.judgePoint24(remainder + [float(nums[j]) / float(nums[i])]):
                    return True

        return False