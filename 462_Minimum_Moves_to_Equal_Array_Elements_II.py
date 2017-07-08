_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a
# move is incrementing a selected element by 1 or decrementing a selected element by 1.

# Sort and remove front and back in pairs. The difference between each pair has to be closed to equal the pair, but the
# meeting point can be anywhere in the gap. Result is that median (or anywhere between 2 medians) is optimal.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        front, back = 0, len(nums) - 1
        moves = 0
        while front < back:
            moves += nums[back] - nums[front]
            front += 1
            back -= 1

        return moves