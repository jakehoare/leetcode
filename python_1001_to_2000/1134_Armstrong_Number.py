_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/armstrong-number/
# The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
# Given a positive integer N, return true if and only if it is an Armstrong number.

# Remove digits by dividing by 10. Add each digit ** length to the result.
# Compare result to original number.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        digits = len(str(N))
        result, n = 0, N

        while n > 0:
            n, digit = divmod(n, 10)
            result += digit ** digits

        return result == N
