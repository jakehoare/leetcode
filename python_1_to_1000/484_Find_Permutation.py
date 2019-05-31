_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-permutation/
# You are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship
# between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was
# constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the
# length of the secret signature plus 1).
# For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by
# array [3,2,4] or [2,1,3,4].
# Your job is to find the lexicographically smallest permutation of [1, 2, ... n] that could refer to the given secret
# signature in the input.

# Using a stack, iterate over integers i to n - 1, pushing each integer. If the next letter is "I", we have reached
# the end of a sequence of "D"s (potentialy of length zero). Pop entire stack and append to result (hence appearing
# in decreasing order).
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        permutation, stack = [], []

        for i in range(1, len(s) + 1):
            stack.append(i)
            if s[i - 1] == "I":
                while stack:
                    permutation.append(stack.pop())

        stack.append(len(s) + 1)
        while stack:
            permutation.append(stack.pop())

        return permutation