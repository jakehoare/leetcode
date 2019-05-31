_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
# We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.
# Note that '0' is not included.
# Now, we write numbers using these digits, using each digit as many times as we want.
# For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.
# Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.

# Iterate over N from the least to most significant digit. For each suffix of N, calculate the number of solutions
# with the same number of digits as the suffix. Attempt to use each digit d of D as the first digit of the suffix.
# If d is less than the first digit of suffix the all combinations of other digits are allowed. If d is the same as the
# first digit of the suffix, the results for the previous suffix are allowed.
# Finally add all solutions that use fewer digits.
# Time - O(log N) (since len(D) is at most 9)
# Space - O(log N)

class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        S = str(N)
        K = len(S)

        dp = [0] * K + [1]  # dp[i] is the result for suffix N[i:] with the same number of digits as N[i:]

        for i in range(K - 1, -1, -1):

            for d in D:

                if d < S[i]:    # every combination of less significant digits is allowed
                    dp[i] += len(D) ** (K - i - 1)
                elif d == S[i]: #
                    dp[i] += dp[i + 1]

        return dp[0] + sum(len(D) ** i for i in range(1, K))    # add solutions with fewer digits

