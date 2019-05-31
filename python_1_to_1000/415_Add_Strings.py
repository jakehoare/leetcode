_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-strings/
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Reverse the numbers so we start iterating over the least significant digit. Pad the shorter number with leading zeros.
# Add each pair of digits plus carry, mod 10 to update the carry. Append the final carry then reverse the result.
# Time - O(max(m, n)) where m and n are the lengths of the input strings
# Space - O(max(m, n))

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]

        length_diff = len(num1) - len(num2)
        if length_diff < 0:
            num1 += "0" * -length_diff
        else:
            num2 += "0" * length_diff

        result, carry = [], 0
        for d1, d2 in zip(num1, num2):
            carry, digit = divmod(int(d1) + int(d2) + carry, 10)
            result.append(str(digit))

        if carry:
            result.append(str(carry))

        return "".join(result[::-1])
