_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
# It's guaranteed that a unique mapping will always exist.

# Iterate along s. If the char at position i + 2 is "#" then convert s[i:i + 2] to an integer.
# Else convert s[i] to an integer.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        n = len(s)
        i = 0

        while i < n:
            if i + 2 < n and s[i + 2] == "#":
                result.append(chr(int(s[i:i + 2]) + ord("a") - 1))
                i += 3
            else:
                result.append(chr(int(s[i]) + ord("a") - 1))
                i += 1

        return "".join(result)