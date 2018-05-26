_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/special-binary-string/
# Special binary strings are binary strings with the following two properties:
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and
# swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the
# first character of the second string.)
# At the end of any number of moves, what is the lexicographically largest resulting string possible?

# Create a list of all optimal special strings, sort in order of most starting 1s and join.
# To create an optimal special string, iterate over S finding the point there the next balance of 1s minus 0s falls to
# zero. Remove the leading 1 and trailing 0 and recurse on the middle part. Middle part is a special string because
# A) it has an equal number of 1s and 0s and B) if a prefix of the middle has one less 1 and 0, it will already be
# processed, so every prefix of middle has as many 1s as 0s, which is the definition of a special string.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        specials = []

        if not S:
            return ""

        balance, start = 0, 0
        for i, c in enumerate(S):

            balance += 1 if c == "1" else -1
            if balance == 0:
                specials.append("1" + self.makeLargestSpecial(S[start + 1:i]) + "0")
                start = i + 1

        specials.sort(reverse = True)
        return "".join(specials)
