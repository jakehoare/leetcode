_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/base-7/
# Given an integer, return its base 7 string representation.

# Record if num is negative and convert to positive. Repeatedly divide by 7 and add digit to result. Result is in
# reverse order with least significant digit first. Add leading minus sign is negative, reverse list and join.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        negative = num < 0                      # flag for negative num
        num = abs(num)
        base_7 = []

        while num:
            num, digit = divmod(num, 7)
            base_7.append(str(digit))

        if negative:
            base_7.append("-")

        return "".join(base_7[::-1]) or "0"     # base_7 is empty if num == 0