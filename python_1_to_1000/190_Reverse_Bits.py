_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-bits/
# Reverse bits of a given 32 bits unsigned integer.
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
# return 964176192 (represented in binary as 00111001011110000010100101000000).

# Convert to string of binary.  Reverse and convert base 2 string back to int.
# Alternatively, if bit i is set than add 2**(31-i) to the result.
# Time - O(log n)
# Space - O(log n)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = bin(n)
        binary = binary[2:]             # remove header '0b'
        reversed_binary = binary[::-1] + ''.join(['0' for _ in range(32 - len(binary))])
        return int(reversed_binary, 2)  # convert from base 2


class Solution2:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        reversed, bit = 0, 31

        while n != 0:
            if n % 2 == 1:      # last bit is set
                reversed += 2**bit
            bit -= 1
            n //= 2

        return reversed