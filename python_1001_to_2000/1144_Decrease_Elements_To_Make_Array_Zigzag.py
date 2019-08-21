_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/
# Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.
# An array A is a zigzag array if either:
# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
# Return the minimum number of moves to transform the given array nums into a zigzag array.

# Iterate over array, calculating the cost of making each element lower than its lowest neighbour.
# Add the cost to the total cost of even or odd indices.
# Return the minimum total cost.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [float('inf')] + nums + [float('inf')]
        even_low, odd_low = 0, 0    # moves to make the even and odd indices low

        for i in range(1, len(nums) - 1):
            # decrease nums[i] to 1 less than the lowest neighbour
            cost = max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
            if i % 2 == 0:
                even_low += cost
            else:
                odd_low += cost

        return min(even_low, odd_low)
