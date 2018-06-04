_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/global-and-local-inversions/
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
# Return true if and only if the number of global inversions is equal to the number of local inversions.

# Every local inversion is also a global inversions, so we only need to check is there are any other global inversions
# i.e. inversions separated by more than one index. Track the max value seen before the previous value, if this is
# greater than the current value we haev another global inversions.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        max_before_prev = -1

        for i in range(1, len(A)):

            if A[i] < max_before_prev:
                return False
            max_before_prev = max(max_before_prev, A[i - 1])

        return True
