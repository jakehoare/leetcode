_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/decoded-string-at-index/
# An encoded string S is given.  To find and write the decoded string to a tape,
# the encoded string is read one character at a time and the following steps are taken:
# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
# Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

# Find the index of S where the decoded string is of length at least K. Iterate backwards in S from the found index.
# For every digit, divide the decoded length by the digit and update K to be the remainder when dividing by the new
# length. For every character, return if the decoded string has the required length else decrement the length.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        length = 0
        for index, c in enumerate(S):
            if "0" <= c <= "9":         # multiply the length of the decoded string
                length *= int(c)
            else:                       # increment the length of the decoded string
                length += 1
            if length >= K:
                break

        for i in range(index, -1, -1):  # iterate backwards along S
            c = S[i]
            if "0" <= c <= "9":
                length //= int(c)
                K %= length
            else:
                if K == length or K == 0:   # K == 0 results from modulo
                    return c
                length -= 1