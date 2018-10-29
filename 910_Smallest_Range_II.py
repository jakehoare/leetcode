_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-range-ii/
# Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K,
# and add x to A[i] (only once).
# After this process, we have some array B.
# Return the smallest possible difference between the maximum value of B and the minimum value of B.

# Sort the array (its starting order is irrelevant). For each split point i, the smaller elements A[i] and to the left
# are increased by K. The larger elements A[i + 1] and to the right are decreased by K. Find the minimum of the left
# and right sides, and the maximum of the left and right sides. Update the result with the difference of the maximum
# and minimum if lower than the current result.
# Time - O(n log n)
# Space - O(n)

class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        result = A[-1] - A[0]       # move all elemnts in same direction

        left_min = A[0] + K         # min of left and max of right are fixed
        right_max = A[-1] - K

        for i in range(len(A) - 1):  # A[i] is the last index moved up, A[i + 1] is first moved down

            lower = min(left_min, A[i + 1] - K) # min of left and right
            upper = max(right_max, A[i] + K)    # max of left and right
            result = min(upper - lower, result)

        return result