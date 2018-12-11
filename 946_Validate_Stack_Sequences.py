_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/validate-stack-sequences/
# Given two sequences pushed and popped with distinct values, return true if and only if this could have been the
# result of a sequence of push and pop operations on an initially empty stack.

# Build the stack by iterating over pushed.
# Pop off top off stack whenever it matched the next element of popped.
# At the end, the stack must be empty.
# Time - O(n)
# Space - O(n)

class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i = 0                   # next index of popped

        for num in pushed:

            stack.append(num)
            while stack and stack[-1] == popped[i]:
                i += 1
                stack.pop()

        return i == len(popped) # stack is empty if i == popped()