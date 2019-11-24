_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/encode-number/
# Given a non-negative integer num, Return its encoding string.
# The encoding is done by converting the integer to a string using a secret function
# that you should deduce from the following table:
# num   encoding
# 0     ""
# 1     "0"
# 2     "1"
# 3     "00"
# 4     "01"
# 5     "10"
# 6     "11"
# 7     "000"

# Encoding is the binary representation of num + 1 without the first digit.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        return bin(num + 1)[3:]
