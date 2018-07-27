_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-sum-of-averages/
# We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average
# of each group. What is the largest score we can achieve?
# Note that our partition must use every number in A, and that scores are not necessarily integers.

# Dynamic programming. Base case of k == 1 is the average of the array. For k > 1, try all possible suffix arrays that
# leave at least k - 1 elements in the prefix for the remainder. Calculate the average of the suffix array and add to
# recursion result on prefix.
# Time - O(n**2 * k)
# Space - O(n * k)

class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        memo = {}

        def helper(i, k):                   # max average for A[:i] partitioned into k subarrays

            if (i, k) in memo:
                return memo[(i, k)]

            if k == 1:
                memo[(i, k)] = sum(A[:i]) / float(i)
                return memo[(i, k)]

            best = 0
            for j in range(k - 1, i):       # retains A[:j] for the k - 1 subarrays and calculate average of suffix
                best = max(best, helper(j, k - 1) + sum(A[j:i]) / float(i - j))

            memo[(i, k)] = best
            return best

        return helper(len(A), K)