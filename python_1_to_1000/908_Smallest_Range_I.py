_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-range-i/
# Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
# After this process, we have some array B.
# Return the smallest possible difference between the maximum value of B and the minimum value of B.

# Each element of A can be adjusted by some number in [-K, K]. If the difference between the max and min of A is <= 2K
# then all elements can be equalized. Else the range can be decreased by 2K.
# Time - O(n)
# Space - O(1)

class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        range = max(A) - min(A)
        return max(0, range - 2 * K)