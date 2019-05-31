_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/2-keys-keyboard/
# Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:
#  Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
#  Paste: You can paste the characters which are copied last time.
# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
# Output the minimum number of steps to get n 'A'.

# If n is prime, we can only make it by copying 'A' and pasting it n - 1 times.
# Consider breaking n down to make a single 'A'. If we find a divisor d of n, then from n // d we can take d steps to
# make n 'A's. Repeat this process as many times as possible with each divisor starting from 2, until only 1 'A' left.
# Solution is the sum of the factors (apart from 1).
# Time - O(n)
# Space - O(1)

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        divisor = 2

        while n > 1:
            while n % divisor == 0:
                steps += divisor
                n //= divisor
            divisor += 1

        return steps
