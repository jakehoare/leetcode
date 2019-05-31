_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/consecutive-numbers-sum/
# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# The sum of consecutive numbers (x + 1) + (x + 2) + ... + (x + k) = kx + k(k + 1)//2.
# We seek k and x to make this equation equal to N.
# Rearranging gives kx = N - k(k + 1)//2. Try all values of k from 1 until the RHS of this becomes negative.
# We have a solution if the RHS is divisible by k.
# Time - O(sqrt(n))
# Space - O(1)

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        k = 1                               # start from sequences of length 1
        temp = N - ((k + 1) * k) // 2       # RHS of equation
        result = 0

        while temp >= 0:

            if temp % k == 0:               # RHS is divisible by k, solution found
                result += 1
            k += 1
            temp = N - ((k + 1) * k) // 2

        return result
