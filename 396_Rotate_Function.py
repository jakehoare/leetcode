_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rotate-function/
# Given an array of integers A and let n to be its length.
# Assume Bk to be an array obtained by rotating the array A k positions clock-wise, we define a "rotation function" F
# on A as follow:
#   F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
# Calculate the maximum value of F(0), F(1), ..., F(n-1).

# Calculate the initial rotated_value and sum of all elements. To rotate, every element is incremented and last element
# is reduced from n-1 to zero times.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        rotate_val, sum_A = 0, 0

        for i, num in enumerate(A):
            sum_A += num
            rotate_val += i * num

        max_rotate = rotate_val
        for i in range(len(A) - 1, -1, -1):
            rotate_val += sum_A - (len(A) * A[i])       # last element net n-1 reduction
            max_rotate = max(max_rotate, rotate_val)

        return max_rotate