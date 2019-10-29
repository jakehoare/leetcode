_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-palindrome-iii/
# Given a string s and an integer k, find out if the given string is a K-Palindrome or not.
# A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

# Helper function returns the number of removals to transform the string between s[start] and s[end], inclusive.
# If s[start] is the same as s[end], recurse without both ends.
# Else take the best case of removing either start or end.
# Memoize to avoid repetition.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        memo = {}

        def helper(start, end):
            if start >= end:                # <= 1 char is a palindrome
                return 0
            if (start, end) in memo:
                return memo[(start, end)]

            if s[start] == s[end]:
                result = helper(start + 1, end - 1)
            else:
                result = 1 + min(helper(start + 1, end), helper(start, end - 1))

            memo[(start, end)] = result
            return result

        return helper(0, len(s) - 1) <= k
