_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/decode-ways-ii/
# A message containing letters from A-Z is being encoded to numbers using the following mapping way:
#  'A' -> 1
#  'B' -> 2
#   ...
#  'Z' -> 26
# Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the
# numbers from 1 to 9.
# Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
# Also, since the answer may be very large, you should return the output mod 10**9 + 7.

# Dynamic programming. Iterate over s. New ways to encode = choices for c * existing ways + choices for c and prev_char
# * prev_ways. Note that * cannot encode 0.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ways = 0
        if s[0] == "*":
            ways = 9
        elif s[0] != "0":
            ways = 1
        prev_char = s[0]
        prev_ways = 1

        for c in s[1:]:

            new = 0
            # multiply ways by choices for c
            if c == "*":
                new = 9 * ways
            elif c != "0":
                new = ways

            # multiply prev_ways by choices for c and prev_char
            if prev_char == "*":
                if c == "*":                # 11 to 19 and 21 to 26
                    new += prev_ways * 15
                elif "0" <= c <= "6":       # prev_char is 1 or 2
                    new += prev_ways * 2
                elif "7" <= c <= "9":       # prev_char is 1
                    new += prev_ways

            elif prev_char == "1":
                if c == "*":
                    new += prev_ways * 9
                else:
                    new += prev_ways

            elif prev_char == "2":
                if c == "*":
                    new += prev_ways * 6
                elif c <= "6":
                    new += prev_ways

            new %= 10 ** 9 + 7

            prev_ways, ways = ways, new
            prev_char = c

        return ways