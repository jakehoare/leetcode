_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/mini-parser/
# Given a nested list of integers represented as a string, implement a parser to deserialize it.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# Note: You may assume that the string is well-formed:
# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].

# Evaluate the string to convert to a nested list of ints. If s_eval is an int, return NestedInteger with that int.
# Else create a NestedInteger of an empty list and recursively add all elements of s_eval.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        return self.helper(eval(s))  # eval converts string to expression (nested list of ints)

    def helper(self, s_eval):

        if isinstance(s_eval, int):
            return NestedInteger(s_eval)

        nested = NestedInteger()  # nested is empty list
        for item in s_eval:
            nested.add(self.helper(item))

        return nested