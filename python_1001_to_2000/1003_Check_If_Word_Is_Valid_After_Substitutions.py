_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# We are given that the string "abc" is valid.
# From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.
# (X or Y may be empty.) Then, X + "abc" + Y is also valid.
# If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".
# Examples of invalid strings are: "abccba", "ab", "cababc", "bac".
# Return true if and only if the given string S is valid.

# Maintain a stack of characters seen but are not part of "abc". Iterate over S. When "a" is encountered, add it to the
# stack. For "b", the previous unmatched char must be "a". For "c", there must be "a" and "b" on the stack or else it
# cannot be matched.
# Time - O(n)
# Space - O(n)

class Solution:
    def isValid(self, S: str) -> bool:

        if len(S) % 3 != 0:     # S must consist of an integer number of "abc" strings
            return False

        stack = []

        for c in S:
            if c == "a":
                stack.append(c)
            elif c == "b":
                if stack and stack[-1] == "a":
                    stack.append(c)
                else:
                    return False
            elif c == "c":
                if len(stack) >= 2 and stack[-2:] == ["a", "b"]:
                    stack.pop()     # match with "a" and "b"
                    stack.pop()
                else:
                    return False

        return not stack        # all chars must be matched
