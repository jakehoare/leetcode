_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-turbulent-subarray/
# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# In other words, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements
# in the subarray.
# Return the length of a maximum size turbulent subarray of A.

# Track the longest subarrays where the last move is up and the last move is down.
# For each difference between elements of the array, extend either the up, the down or neither sequence.
# Swap the up and down counts after every iteration, so the next iteration is opposite.
# Time - O(n)
# Space - O(1)

class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:             # special case of single element
            return 1

        result = 0
        down, up = 0, 0             # longest sequences where last move is up and down

        for i in range(1, len(A)):

            if A[i] > A[i - 1]:     # extend up sequence, no down sequence
                up += 1
                down = 0
            elif A[i] < A[i - 1]:   # extend down sequence, no up sequence
                down += 1
                up = 0
            else:                   # extend neither sequence
                down = 0
                up = 0

            result = max(result, up, down)
            up, down = down, up     # swap so next iteration considers opposite move

        return result + 1 if result != 0 else 0     # add 1 for final element only if any sequence found
