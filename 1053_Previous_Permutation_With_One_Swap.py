_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/previous-permutation-with-one-swap/
# Given an array A of positive integers (not necessarily distinct),
# return the lexicographically largest permutation that is smaller than A, that can be made with one swap.
# A swap exchanges the positions of two numbers A[i] and A[j]).
# If it cannot be done, then return the same array.

# Iterate from the least significant digit to the most significant.
# If a digit is grater than the previous digit then A can be made smaller by swapping A[i] with the next smallest
# digit. Search for the next smallest digit, taking the most significant in the event of a tie.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A) - 2, -1, -1):

            if A[i] > A[i + 1]:        # A can be made smaller by swapping a smaller digit to A[i]

                max_seen = -1
                for j in range(len(A) - 1, i, -1):
                    if A[j] >= max_seen and A[j] < A[i]:
                        max_seen = A[j]
                        max_seen_index = j

                A[i], A[max_seen_index] = A[max_seen_index], A[i]   # swap
                break

        return A
