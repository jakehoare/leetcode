_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-array-with-same-average/
# In a given integer array A, we must move every element of A to either list B or list C.
# B and C initially start empty.
# Return true if and only if after such a move, it is possible that the average value of B is equal to the average
# value of C, and B and C are both non-empty.

# For the averages of B and C to be equal, they must both be the average of A.
# For each length of B from 1 to half of the length of A, find the required sum of B. If this is an integer, attempt to
# find numbers in A to make B with the required length and sum with helper function n_sum_target.
# Time - O(n * 2**n) since O(n) lengths of B, for which each element of A may or may not be included
# Space - O(2**n)

class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        def n_sum_target(n, tgt, j):    # helper fn, can we find n numbers in A[j:] that sum to tgt?

            if (n, tgt, j) in invalid:  # already know this is impossible
                return False
            if n == 0:                  # if no more numbers can be chosen,
                return tgt == 0         # then True if and only if we have exactly reached the target

            for i in range(j, len(C)):

                if C[i] > tgt:          # remaining numbers are at least as large because C is sorted
                    break
                if n_sum_target(n - 1, tgt - C[i], i + 1):  # recurse having used num in B
                    return True

            invalid.add((n, tgt, j))
            return False

        n, sum_A = len(A), sum(A)
        invalid = set()                 # memoize failed attempts
        C = sorted(A)                   # C initially contains all of A

        for len_B in range(1, (n // 2) + 1):  # try all possible lengths of B

            target = sum_A * len_B / float(n)
            if target != int(target):  # target must be an integer
                continue

            if n_sum_target(len_B, target, 0):
                return True

        return False