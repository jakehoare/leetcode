_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/utf-8-validation/
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
#   For 1-byte character, the first bit is a 0, followed by its unicode code.
#   For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most
#   significant 2 bits being 10.
# Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

# If first bit set then count number of leading 1s, not 1 or more than 4, check following bytes start with 10
# Time - O(n)
# Space - O(1)

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):

            byte = data[i]

            if byte & (1 << 7) == 0:        # first bit is a zero
                i += 1
                continue

            bit = 6
            while byte & (1 << bit) and bit > 3:
                bit -= 1
            if byte & (1 << bit) or bit == 6:   # 1 or more than 4 leading 1 bits
                return False

            bytes = 6 - bit     # expeted number of bytes starting with 10
            i += 1
            while bytes:
                if i >= len(data) or data[i] & (128 + 64) != 128:
                    return False
                bytes -= 1
                i += 1

        return True
