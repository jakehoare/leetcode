_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/monotonic-array/
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return true if and only if the given array A is monotonic.

# Iterate an check all A[i] >= A[i + 1] or A[i] <= A[i + 1]
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))