_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# A sequence X_1, X_2, ..., X_n is fibonacci-like if:
# n >= 3
# X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
# Given a strictly increasing array A of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of A. If one does not exist, return 0.
# Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none)
# from A, without changing the order of the remaining elements.

# For each pair of numbers, attempt to build a Fibonacci sequence. Copy the integers into a set for O(1) lookup when
# testing if a sequence can be extended.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A_set = set(A)
        max_length = 0

        for i, num in enumerate(A):

            for num2 in A[i + 1:]:

                prev_num = num2
                next_num = num + num2
                length = 2
                while next_num in A_set:    # sequence can be extended
                    length += 1
                    next_num, prev_num = next_num + prev_num, next_num

                max_length = max(max_length, length)

        return max_length if max_length >= 3 else 0