_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# We are given an array A of positive integers, and two positive integers L and R (L <= R).
# Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that
# subarray is at least L and at most R.

# Dynamic programming. Find the number of solutions ending with each element of A. If the element is greater than R
# then there are no solutions and we record the index of the latest element greater than R. If the element is less than
# L then every solution ending with the previous element can be extended. If the element is between L and R inclusive
# then every subarray starting after the last element greater than R is a solution.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        subarrays, total = 0, 0 # subarrays ending at current index, grand total
        last_above_max = -1     # index of last element > R

        for i, num in enumerate(A):

            if num > R:
                subarrays = 0
                last_above_max = i

            elif num < L:       # all subarrays ending at previous index cn be extended
                total += subarrays

            else:               # count subarrays ending with i and starting after last_above_max
                subarrays = i - last_above_max
                total += subarrays

        return total
