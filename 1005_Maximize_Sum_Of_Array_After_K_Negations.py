_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
# Given an array A of integers, we must modify the array in the following way: we choose an i and
# replace A[i] with -A[i], and we repeat this process K times in total.
# We may choose the same index i multiple times.
# Return the largest possible sum of the array after modifying it in this way.

# Sort the array in ascending order. Iterate along the array flipping all negative elements to positive until no more
# flips are required or there are no more negatives. If there are an odd number of flips remaining, flip the smallest
# element, which is either the last element flipped (if any) or the next element.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()

        i = 0
        while K > 0 > A[i]:     # K positive and A[i] negative
            A[i] = -A[i]
            i += 1
            K -= 1

        result = sum(A)
        if K % 2 == 1:
            result -= 2 * min(A[i], float("inf") if i == 0 else A[i - 1])

        return result