_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Repeatedly remove each digit and update the product and total sum.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        product, total = 1, 0

        while n > 0:                # note n can be positive only
            n, digit = divmod(n, 10)
            product *= digit
            total += digit

        return product - total
