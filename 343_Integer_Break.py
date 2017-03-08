_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/integer-break/
# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product
# of those integers. Return the maximum product you can get.

# For numbers > 4, subtract as many 3s as possible since any larger number should itself be broken and 3*3 > 2*2*2 so
# subtracting 3s is better than 2s.
# Alternatively, dynamic programming to try all splits.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1

        threes, remainder = divmod(n - 4, 3)
        product = 3**threes
        remainder += 4

        if remainder == 4:
            return product * 2 * 2
        if remainder == 5:
            return product * 3 * 2
        return product * 3 * 3


class Solution2(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_breaks = [0, 1]

        for i in range(2, n + 1):
            max_break = 0

            for j in range(1, (i // 2) + 1):
                # either split k or keep, same for i - j
                max_break = max(max_break, max(j, max_breaks[j]) * max(i - j, max_breaks[i - j]))

            max_breaks.append(max_break)

        return max_breaks[-1]