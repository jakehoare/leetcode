_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convert-to-base-2/
# Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).
# The returned string must have no leading zeroes, unless the string is "0".

# In base -2 a number is expressed as a + -2*b + 4*c + -8*d + 16*e + ... for some bits a, b, c, d, e ...
# Repeatedly divide by 2 to determine if the least significant bit should be set. Flip the sign of the number after
# each division so the next number becomes b + -2*c + 4*d + -8*e + ... and repeat until zero.
# Bits are found in order from least to most significant, so reverse the result.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"
        result = []

        while N != 0:
            N, bit = divmod(N, 2)
            N *= -1
            result.append(str(bit))

        return "".join(reversed(result))
