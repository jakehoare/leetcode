_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)
# Return the largest string X such that X divides str1 and X divides str2.

# Find the GCD of the lengths of the strings.
# Check whether both strings consist of repeated prefix of GCD length.
# Time - O(m + n)
# Space - O(1)

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        a, b = len(str1), len(str2)
        if a < b:
            a, b = b, a

        while b != 0:
            a, b = b, a % b

        candidate = str1[:a]
        return candidate if str1 == candidate * (len(str1) // a) and str2 == candidate * (len(str2) // a) else ""
