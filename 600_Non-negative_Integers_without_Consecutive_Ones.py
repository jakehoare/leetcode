_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
# Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary
# representations do NOT contain consecutive ones.

# Use dynamic programming to calculate the number of integers without repeated set bits and with most significant bit
# of 0 and of 1, up to the same number of bits as num.
# Also dynamically update count of valid integers as num is extended from least significant bit. If last bit is zero,
# keep count unchanged. If last bits are "11" then reset count since all valid integers ending in zero and one with
# this length are possible. If last bits are "01" then valid integers ending in 1 are all previous valid integers
# extended by one, valid integers ending in zero are all valid integers of this length ending in zero.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        # remove "0b" prefix and reverse so least significant bit has lowest index
        binary = bin(num)[2:][::-1]

        # zero_highest[i] is the number of non-negative integers with i + 1 bits and highest bit of zero
        # that do not contain consecutive set bits. Note that zero_highest[i - 1] overlaps with and is a
        # subset of zero_highest[i]
        zero_highest = [1]
        one_highest = [1]

        if binary[0] == "0":
            count = 1
        else:
            count = 2

        for bit in range(1, len(binary)):  # iterate over prefixes from least significant bit

            # can append zero to all shorter valid numbers ending in zero or one
            zero_highest.append(zero_highest[-1] + one_highest[-1])
            # can only append one to all shorter valid numbers ending in zero
            one_highest.append(zero_highest[-2])

            if binary[bit] == "1" and binary[bit - 1] == "1":
                # prefix ends in "11" so all integers of same length or shorter
                # without consecutive set bits are less than prefix regardless of ending in 0 or 1.
                # reset count to all valid integers
                count = zero_highest[-1] + one_highest[-1]

            elif binary[bit] == "1" and binary[bit - 1] == "0":
                # prefix ends in "10" so can append "1" to all previous integers
                # plus can add all integers of this length ending with "0"
                count += zero_highest[-1]

                # else if most significant bit of prefix is "0" then count is unchanged
                # but no incermentail new integers are valid

        return count