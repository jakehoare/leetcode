_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/1-bit-and-2-bit-characters/
# We have two special characters. The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not.
# The given string will always end with a zero.

# If the first bit is 1, it must be a 2-bit character so move 2 spaces forwards. Else move one space forwards.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:

            if bits[i] == 1:
                i += 1
            i += 1

        return i == len(bits) - 1