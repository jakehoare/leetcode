_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/
# Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)
# For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes
# at the end. Given K, find how many non-negative integers x have the property that f(x) = K.

# Binary search for the smallest x such that f(x) >= K. If f(x) == K then there is some integer with K trailing zeros
# hence there are 5 such integers (the integers between successive factors of 5). Else there is no integer with K
# trailing zeros.
# Time - O(log^2 K), log K for factorial_zeros and log K for binary search
# Space - O(1)

class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        def factorial_zeros(n):         # find the number of trailing zeros in n!, as per problem 172
            factor = 5
            result = 0
            while factor <= n:
                result += n // factor
                factor *= 5
            return result

        left, right = 0, 10 * K         # solution is approximately 5 * K

        while left < right:             # loop until only one candidate remains

            mid = (left + right) // 2
            mid_zeros = factorial_zeros(mid)
            if mid_zeros < K:           # check strictly greater integers
                left = mid + 1
            else:                       # mid remains in range
                right = mid

        return 5 if factorial_zeros(right) == K else 0
