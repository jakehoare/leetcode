_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convert-a-number-to-hexadecimal/
# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method
# is used.
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
# character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.

# Repeatedly divide by 16, converting the remainder to a digit or letter (if > 9). Reverse the result so most
# significant bit is first.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:        # special case, while loop is not entered
            return "0"
        if num < 0:         # 2s complement of negative numbers
            num += 2 ** 32

        result = []

        while num != 0:

            num, digit = divmod(num, 16)
            if digit > 9:   # convert to char
                result.append(chr(ord("a") + digit - 10))
            else:
                result.append(str(digit))

        return "".join(result[::-1])    # reverse