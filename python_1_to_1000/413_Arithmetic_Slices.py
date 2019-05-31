_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/arithmetic-slices/
# A sequence of number is called arithmetic if it consists of at least three elements and if the difference between
# any two consecutive elements is the same.
# Return the number of arithmetic slices in the array.

# If the current diff is the same as the previous, add to result all slices ending here. Else reset progression start.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0

        diff = A[1] - A[0]
        start, slices = 0, 0  # start of current progression

        for i in range(2, n):

            next_diff = A[i] - A[i - 1]

            if next_diff == diff:
                slices += i - start - 1
            else:
                diff = next_diff
                start = i - 1

        return slices