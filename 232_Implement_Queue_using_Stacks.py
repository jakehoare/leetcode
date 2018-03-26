_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/implement-queue-using-stacks/
# Implement the following operations of a queue using stacks.
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# You may assume that all operations are valid (e.g., no pop or peek operations will be called on an empty queue).

# One stack contains the iteams as they are added. Another stack is used to reverse the order during the pop operation.
# The top of the stack is recorded for O(1) peek.
# Time - O(1) for init, push, peek and empty. O(n) for pop.
# Space - O(n)

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.reversed = []
        self.top = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.top = x
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.reversed:
            while self.stack:
                self.reversed.append(self.stack.pop())
        return self.reversed.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.reversed:
            return self.reversed[-1]
        return self.top

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack and not self.reversed