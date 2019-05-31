_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-width-ramp/
# Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].
# The width of such a ramp is j - i.
# Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

# If a later element of A is greater than or equal to an earlier element then the earlier element makes a wider ramp.
# Hence we find the indices of strictly decreasing elements of A, which are candidates for the left edges of ramps.
# Then iterate over A again from the last index to the first, considering each element as the right edge of a ramp.
# When an element is greater than the top of stack, update max_ramp and pop off top of stack since lower index
# elements of A cannot make wider ramps.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        max_ramp = 0
        stack = []                              # stack of indices in decreasing value order, left edges of ramps

        for i, num in enumerate(A):
            if not stack or num < A[stack[-1]]:
                stack.append(i)

        for i in range(len(A) - 1, -1, -1):     # iterate backwards
            while stack and A[i] >= A[stack[-1]]:
                max_ramp = max(max_ramp, i - stack.pop())

        return max_ramp