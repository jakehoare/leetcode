_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-two-integers/
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Use mask to isolate 32 bits. Sum of 2 bits is the XOR. If both bits are set, carry to next bit. Repeat until no
# more carry. Ir result is more than MAX_INT, subtract 2**32.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF       # 2**32 - 1
        MAX_INT = 0x7FFFFFFF    # 2**31 - 1

        while b != 0:

            total = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK   # shift pattern when both bits are set
            print(a, b, total, carry)
            a, b = total, carry

        return a if a < MAX_INT else ~(a ^ MASK)    # a - 2**321

