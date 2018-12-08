_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
# Return the least number of moves to make every value in A unique.

# Iterate over the sorted numbers. If a number is more than that last number used, it does not need incrementing.
# Else increment it to last_used + 1. In both cases update last_used.
# Time - O(n log n)
# Space - O(n)

class Solution:
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        increments = 0
        last_used = -1

        for num in sorted(A):

            if num <= last_used:
                increments += last_used + 1 - num
                last_used += 1
            else:
                last_used = num

        return increments