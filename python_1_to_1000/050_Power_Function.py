_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/powx-n/
# Implement pow(x, n).

# Recursively calculate (pow(x, n//2))^2 if n is even or with additional factor of x if n is odd.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        neg = n < 0
        pos_result = self.pos_pow(x, abs(n))
        return 1/pos_result if neg else pos_result

    def pos_pow(self, x, n):
        if n == 0:
            return 1

        temp = self.pos_pow(x, n//2)
        temp *= temp

        return temp if n % 2 == 0 else temp * x
