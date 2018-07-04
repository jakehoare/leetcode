_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# We have two integer sequences A and B of the same non-zero length.
# We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their
# respective sequences.
# At the end of some number of swaps, A and B are both strictly increasing.
# A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].
# Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
# It is guaranteed that the given input always makes it possible.

# Dynamic programming. For each index, find the minimum swaps to make an increasing sequence to (and including) that
# index, with and without swapping elements at that index.
# If the elements at index i in A and B are both increasing relative to their previous elements, the cost without
# swapping is the previous cost without swapping and the cost with swapping is 1 + the previous cost with swapping
# (since if i and i-1 are swapped then the lists are in the origina order). If the lists are increasing after swapping
# at index i, update the cost without swapping according to the previous cost with swapping, and the cost with swapping
# as 1 + the previous cost without swapping.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        prev_no_swap, prev_swap = 0, 1              # min swaps without and with swapping at first index

        for i in range(1, len(A)):                  # start from second index

            no_swap, swap = float("inf"), float("inf")  # default infinity if no increasing subsequences can be made

            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                no_swap = prev_no_swap
                swap = 1 + prev_swap

            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                no_swap = min(no_swap, prev_swap)
                swap = min(swap, 1 + prev_no_swap)

            prev_no_swap, prev_swap = no_swap, swap

        return min(prev_no_swap, prev_swap)
