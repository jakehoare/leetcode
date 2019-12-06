_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/hexspeak/
# A decimal number can be converted to its Hexspeak representation
# by first converting it to an uppercase hexadecimal string,
# then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.
# Such a representation is valid if and only if it consists only of the letters in the set
# {"A", "B", "C", "D", "E", "F", "I", "O"}.
# Given a string num representing a decimal integer N,
# return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

# Convert to hex.
# Return ERROR if any digit apart from 0 or 1 remains.
# Replace 0 with O and replace 1 with I.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        s = format(int(num), "X")       # upper case hex without 0X prefix.
        if any(str(i) in s for i in range(3, 10)):
            return "ERROR"
        s = s.replace("0", "O")
        return s.replace("1", "I")
