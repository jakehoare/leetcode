_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/license-key-formatting/
# You are given a string S, which represents a software license key which we would like to format. The string S is
# composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string
# into groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are
# possibly misplaced.
# We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but
# still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all
# the lower case letters in the string must be converted to upper case.
# You are given a non-empty string S, representing a license key to format, and an integer K. And you need to
# return the license key formatted according to the description above.

# Replace "-" by "" and convert to upper case. Append complete blocks of length K to result working from back of string.
# If any stub append that, reverse blocks and join.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        key = S.replace("-", "").upper()
        formatted = []

        i = len(key) - K
        while i >= 0:
            formatted.append(key[i:i + K])
            i -= K

        if i != -K:
            formatted.append(key[:i + K])
        return "-".join(formatted[::-1])

        return "-".join(formatted)


