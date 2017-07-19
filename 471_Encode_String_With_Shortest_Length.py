_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/encode-string-with-shortest-length/
# Given a non-empty string, encode the string such that its encoded length is the shortest.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
# repeated exactly k times.
# k will be a positive integer and encoded string will not be empty or have extra space.
# You may assume that the input string contains only lowercase English letters.
# If an encoding process does not make the string shorter, then do not encode it.
# If there are several solutions, return any of them is fine.

# Take the minumum length of 3 possible encoding types:
# 1) If s consists entirely of a repeated substring, encode as that substring with recursion.
# 2) For all breakpoints in s, recursively encode LHS and RHS
# 3) s without encoding
# Memoise results.

# Time - O(n**3) every one of O(n**2) substring is encoded, taking O(n) time to construct each.
# Space - O(n**3)

class Solution(object):
    def encode(self, s, memo = {}):     # amend signature to add memo, empty by default
        """
        :type s: str
        :rtype: str
        """
        if s in memo:
            return memo[s]

        encodings = [s]                 # list of possible encodings
        i = (s + s).find(s, 1)          # repeated substring problem
        if i != -1 and i != len(s):     # s consists of a repeated substring (which is not s itself)
            encodings.append(str(len(s) / i) + "[" + self.encode(s[:i], memo) + "]")    # recurse

        for i in range(1, len(s)):      # all possible break points
            encodings.append(self.encode(s[:i], memo) + self.encode(s[i:], memo))

        result = min(encodings, key = len)  # minimum length of all encodings
        memo[s] = result
        return result