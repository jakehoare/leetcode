_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-the-closest-palindrome/
# Given an integer n, find the closest integer (not including itself), which is a palindrome.
# The 'closest' is defined as absolute difference minimized between two integers.
# The input n is a positive integer represented by string, whose length will not exceed 18.
# If there is a tie, return the smaller one as answer.

# There are 5 possible candidates.
# 1) A number 1 digit shorter than n of all 9s
# 2) A number 1 digit longer than n ending and starting in 1 with all other zeros
# 3) Reversed LHS replacing RHS and middle digit(s) same
# 4) as 3) but middle index incremented
# 5) as 3) but middle index decremented
# Make all candidates that exist (care of single digit n, 0 and 9 in middle. If length is odd them middle is a
# single digit, else it is a pair.
# Find closest of candidates or lower if tie.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        digits = len(n)
        candidates = {int("1" + "0" * (digits - 1) + "1")}  # longer length e.g. 88 -> 101
        if len(n) > 1:
            candidates.add(int("9" * (digits - 1)))  # shorter length e.g. 12 -> 9

        mid = len(n) // 2  # middle index if odd length, or first of RHS if even
        left = n[:mid]

        if len(n) % 2 == 1:
            centre_count = 1  # odd, so single middle index
            centre = n[mid]
            right = left[::-1]
        else:
            centre_count = 2  # even, so pair of middle indices
            centre = left[-1]
            left = left[:-1]
            right = left[::-1]

        candidates.add(int(left + centre * centre_count + right))
        if centre != "9":
            new_centre = str(int(centre) + 1)
            candidates.add(int(left + new_centre * centre_count + right))
        if centre != "0":
            new_centre = str(int(centre) - 1)
            candidates.add(int(left + new_centre * centre_count + right))

        n_int = int(n)
        candidates.discard(n_int)
        candidates = list(candidates)
        candidates.sort(key=lambda x: (abs(x - n_int), x))  # sort by (abs difference from n, value)
        return str(candidates[0])