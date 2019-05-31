_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sort-array-by-parity-ii/
# Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
# You may return any answer array that satisfies this condition.

# Iterate over even indices, tracking the next odd index to be checked. If the value at an even index is not even,
# find the next odd index that is not odd and swap values.
# Time - O(n)
# Space - O(n)

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = 1

        for even in range(0, len(A), 2):

            if A[even] % 2 == 1:

                while A[odd] % 2 == 1:
                    odd += 2
                A[odd], A[even] = A[even], A[odd]

        return A