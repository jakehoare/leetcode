_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between
# any two consecutive elements is the same.
# A zero-indexed array A consisting of N numbers is given. A subsequence slice of that array is any sequence of
# integers (P0, P1, ..., Pk) such that 0 ≤ P0 < P1 < ... < Pk < N.
# A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic if the sequence A[P0], A[P1], ...,
# A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.
# The function should return the number of arithmetic subsequence slices in the array A.

# For each num, create a dictionary mapping arithmetic progression differences to the count of APs of length >= 2 and
# ending at num. For each num find the diff from all previous nums.  All APs of length >= 2 ending at previous num
# with that diff can be extended to make a valid subsequence slice. All APs form new APs ending at num plus the new
# AP from A[i] to A[j].
# Time - O(n**2)
# Space - O(n**2)

from collections import defaultdict

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        subsequences = []   # list of dicts, each dict maps from a difference value to the count of subsequence slices
                            # ending at A[i] with that difference and of length 2 or more
        for i in range(len(A)):
            subsequences.append(defaultdict(int))

            for j in range(i):                                  # for each previous num
                diff = A[i] - A[j]
                diff_count = subsequences[j].get(diff, 0)       # default to zero
                count += diff_count             # all sequences (length 2 or more) can be extended and end here
                subsequences[-1][diff] += diff_count + 1        # add new sequence from i to j

        return count