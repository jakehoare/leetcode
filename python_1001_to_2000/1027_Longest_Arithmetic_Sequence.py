_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-arithmetic-sequence/
# Given an array A of integers, return the length of the longest arithmetic subsequence in A.
# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1,
# and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

# For each element of the array, maintain a mapping from a subsequence difference to the length of the subsequence.
# For each pair of elements, calculate the difference between their values.
# Update the mapping for the later element with the greater of its current length and 1 + the length of the
# subsequence ending at the earlier element.
# The result is the maximum length from all sequences, plus one since we have counted the number of difference in a
# subsequence and require the number of elements.
# Time - O(n**2)
# Space - O(n**2)

from collections import defaultdict

class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # map sequence difference to its length for each element of A
        sequences = [defaultdict(int) for _ in range(len(A))]

        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]      # difference between successive elements of the subsequence
                sequences[i][diff] = max(sequences[j][diff] + 1, sequences[i][diff])

        return max(max(mapping.values()) for mapping in sequences[1:]) + 1
