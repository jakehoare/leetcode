_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/decode-ways/
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# Dynamic programming.  Calc ways for prefix of length i from prefixes of lengths i-1 and i-2.
# Time - O(n)
# Space - O(n), could be O(1) by keeping only last 2 values of nb_ways

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        nb_ways = [0] * (len(s)+1)      # nb_ways[i] is number of ways to decode prefix of length i
        nb_ways[0] = 1                  # required else '10' will be 0
        if s[0] != '0':
            nb_ways[1] = 1

        for i in range(1, len(s)):

            if s[i] != '0':                     # last char is not '0'
                nb_ways[i+1] += nb_ways[i]      # use all ways to decode without this char
            if 10 <= int(s[i-1:i+1]) <= 26:     # last 2 form int between 10 and 26
                nb_ways[i+1] += nb_ways[i-1]    # use all ways to decode without last 2 chars

        return nb_ways[-1]
