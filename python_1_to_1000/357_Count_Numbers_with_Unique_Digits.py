_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-numbers-with-unique-digits/
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10**n.

# For a single digit there are 10 choices.  For exactly 2 digits, all of the single digit results apart from 0 can have
# any of the 9 unused digit appended.  For exactly 3 digits we can append any of the 8 unused digits to each of the
# 2 digit solutions.  With more than 10 digits there are no more uniquie combinations.
# Time - O(1) since at most 10 digits
# Space - O(1)

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        uniques = 10        # for 1 digit
        can_expand = 9      # numbers that can be expanded by adding another digit

        for digits in range(2, min(n, 10) + 1):     # no increase after used all digits
            can_expand *= (11 - digits)
            uniques += can_expand

        return uniques

