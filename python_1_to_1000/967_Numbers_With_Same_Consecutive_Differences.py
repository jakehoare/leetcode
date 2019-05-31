_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
# Return all non-negative integers of length N such that the absolute difference between every two consecutive
# digits is K.
# Note that every number in the answer must not have leading zeros except for the number 0 itself.
# For example, 01 has one leading zero and is invalid, but 0 is valid.
# You may return the answer in any order.

# Starting from each of the digits apart from zero, repeatedly add and subtract K to the last_digit of each number to
# build up the results to N digits.
# Time - O(2**n)
# Space - O(2**n)

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        partials = [i for i in range(1, 10)]

        for _ in range(N - 1):
            new_partials = []

            for p in partials:

                last_digit = p % 10
                if last_digit - K >= 0:
                    new_partials.append(p * 10 + last_digit - K)
                if K != 0 and last_digit + K < 10:
                    new_partials.append(p * 10 + last_digit + K)

            partials = new_partials

        if N == 1:
            partials.append(0)

        return partials
