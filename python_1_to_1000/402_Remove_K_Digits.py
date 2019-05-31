_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-k-digits/
# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
# is the smallest possible.

# Iterate over num. If previous digit > current digit then preferable to remove previous digit provided k is +ve.
# This creates result in non-descending order. Add all digits to result.
# If any k remain, remove least significant digits. Remove leading zeros.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []

        for c in num:

            while k and result and result[-1] > c:
                result.pop()
                k -= 1

            result.append(c)

        while k:
            result.pop()
            k -= 1

        return "".join(result).lstrip("0") or "0"       # "0" if result is empty