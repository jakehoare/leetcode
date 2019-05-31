_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/wiggle-subsequence/
# A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate
# between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence
# with fewer than two elements is trivially a wiggle sequence.
# Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence
# is obtained by deleting some number of elements (potentially zero) from the original sequence, leaving the remaining
# elements in their original order.

# If next move is in opposite direction to previous move then increase max_length.  If not then update previous so
# the last element of the increasing/decreasing/same subsequence is used.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_length = 1
        prev = nums[0]
        direction = 0  # last move undetermined, +1 = up, -1 = down

        for num in nums[1:]:
            if direction != -1 and num < prev:
                max_length += 1
                direction = -1
            elif direction != 1 and num > prev:
                max_length += 1
                direction = 1
            prev = num

        return max_length