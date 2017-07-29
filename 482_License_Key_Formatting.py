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

# Replace "-" by "" and convert to upper case.
# Time - O(n**2 / K) since n // K blocks and each concatenation takes O(n)
# Space - O(n)

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        key = S.replace("-", "").upper()

        blocks, stub = divmod(len(key), K)
        if stub == 0:           # set stub to a block if zero to avoid leading "-"
            stub = K
            blocks -= 1
        formatted = key[:stub]

        for i in range(blocks):
            formatted += "-" + key[(i * K) + stub:((i + 1) * K) + stub]

        return formatted