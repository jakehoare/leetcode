_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/plus-one/
# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list.

# Starting from least significant digit, replace with zeros until we find the first non 9, which is incremented.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i == -1:
            return [1] + digits
        return digits[:i] + [digits[i]+1] + digits[i+1:]
