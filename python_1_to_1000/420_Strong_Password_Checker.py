_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/strong-password-checker/
# A password is considered strong if below conditions are all met:
# It has at least 6 characters and at most 20 characters.
# It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It must NOT contain three repeating characters in a row.
# Write a function that takes a string s as input, and return the MINIMUM change required to make s a strong password.
# If s is already strong, return 0.
# Insertion, deletion or replace of any one character are all considered as one change.

# For difficult case of length > 20. Use required deletions to reduce the number of substitutions required.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        upper, lower, digit = False, False, False
        subs, i = 0, 0  # nb subs to remove sequences, index counter
        singles, doubles = 0, 0  # nb single and double deletions

        while i < len(s):

            if s[i].isdigit():
                digit = True
            if s[i].isupper():
                upper = True
            if s[i].islower():
                lower = True

            if i >= 2 and s[i] == s[i - 1] == s[i - 2]:  # sequence of 3
                seq = 2
                while i < len(s) and s[i] == s[i - 1]:  # find length of sequence
                    seq += 1
                    i += 1

                subs += seq // 3
                if seq % 3 == 0:
                    singles += 1
                if seq % 3 == 1:
                    doubles += 1

            else:
                i += 1

        types_missing = 3 - (digit + upper + lower)

        if len(s) < 6:
            return max(types_missing, 6 - len(s))
        if len(s) <= 20:
            return max(types_missing, subs)

        deletions = len(s) - 20

        subs -= min(deletions, singles)
        subs -= min(max(deletions - singles, 0), doubles * 2) / 2
        subs -= max(deletions - singles - 2 * doubles, 0) / 3

        return deletions + max(types_missing, subs)
