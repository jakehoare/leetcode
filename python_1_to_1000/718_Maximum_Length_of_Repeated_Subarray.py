_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

# Binary search for the largest length of a mutual subarray in A and B.
# Time - O(log(min(m, n)) * (m + n) * min(m, n))
# Space - O(m**2)

class Solution(object):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    def findLength(self, A, B):

        def mutual_subarray(length):
            # make all subarrays of length in A
            subarrays = set(tuple(A[i:i + length])
                            for i in range(len(A) - length + 1))
            # check if any of same length are also in B
            return any(tuple(B[j:j + length]) in subarrays
                       for j in range(len(B) - length + 1))

        low, high = 0, min(len(A), len(B)) + 1

        while low < high:   # search for smallest length with no mutual subarray

            mid = (low + high) // 2

            if mutual_subarray(mid):    # mid has mutual subarray so search above mid
                low = mid + 1
            else:
                high = mid              # mid does not have mutual subarray so search mid and below

        return low - 1
