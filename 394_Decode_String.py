_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/decode-string/
# Given an encoded string, return it's decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Build stack of chars of result. Iterate over input, pushing chars to stack.
# Parse digits to an integer until opening bracket, then push integer to stack and reset.
# If closing bracket, pop chars until integer is found then push back char sequence multiplied by integer.
# Alternatively, recursively.
# Time - O(2**n), integer creates sequence of length 2**n
# Space - O(2**n)

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        repeats = 0
        digits = set("0123456789")

        for c in s:

            if c == "]":
                item = stack.pop()
                current = []
                while not isinstance(item, int):
                    current.append(item)
                    item = stack.pop()
                stack += (current[::-1] * item)

            elif c in digits:
                repeats = repeats * 10 + int(c)

            elif c == "[":              # must have preceeding integer
                stack.append(repeats)
                repeats = 0

            else:
                stack.append(c)

        return "".join(stack)


class Solution2(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.i = 0  # next index in s to be decoded
        return "".join(self.decode(s))

    def decode(self, s):
        result = []

        while self.i < len(s) and s[self.i] != "]":     # loop until end of s or closing bracket

            if s[self.i] not in "0123456789":           # add characters to result
                result.append(s[self.i])
                self.i += 1
            else:
                repeats = 0
                while s[self.i] in "0123456789":        # calculate number of repetitions
                    repeats = repeats * 10 + int(s[self.i])
                    self.i += 1
                self.i += 1                             # skip over "["
                result += (self.decode(s) * repeats)    # recurse inside brackets and repeat
                self.i += 1                             # skip over "]"

        return result
