_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/integer-replacement/
# Given a positive integer n and you can do operations as follow:
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?

# If n is even, half it. If (n-1)%4 == 0 then the last 2 bits of n are 01, decrementing will make the last 2 bits 00
# which is better than incrementing to make last 2 bits 10.
# If (n-1)%4 != 0 then the last 2 bits of n are 11, decrementing will make the last 2 bits 10, incrementing will
# make the last 2 bits 00 and carry will at worst change one bit from 0 to 1 but potentiall reduce the number of set
# bits. Incrementing is at least as good as decrementing.
# 3 is the exception where n-1 is not divisible by 4 bit it is still better to decrement.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        operations = 0

        while n > 1:

            operations += 1

            if n % 2 == 0:
                n //= 2

            elif n == 3 or (n - 1) % 4 == 0:
                n -= 1

            else:
                n += 1

        return operations