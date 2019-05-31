_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

# Main stack has all items, mins stack has items less than or equal to previous min.
# Note : no error handling for empty stack required
# Time - O(1)
# Space - O(n)

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main = []
        self.mins = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.main.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self):
        """
        :rtype: void
        """
        item = self.main.pop()
        if item == self.mins[-1]:
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.main[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]