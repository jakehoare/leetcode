_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/132-pattern/
# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k
# and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a
# 132 pattern in the list.

# Iterate over nums in reverse order. If num < two then we have a solution because some number greater than two was
# seen after two (and caused two to be popped off stack). Stack is ascending from top to bottom, so last pop is
# greatest number less than num.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        two = float("-inf")
        stack = []

        for i in range(len(nums) - 1, -1, -1):

            if nums[i] < two:
                return True

            while stack and stack[-1] < nums[i]:
                two = stack.pop()

            stack.append(nums[i])

        return False