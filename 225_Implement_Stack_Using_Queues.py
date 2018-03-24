_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/implement-stack-using-queues/
# Implement the following operations of a stack using queues.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size,
# and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or
# deque (double-ended queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

# To insert, append to deque. To pop, move ell elements to new_queue until there is only one element and return that.
# To top, similar to pop except all elements are moved to new_queue. After pop or top, set queue to new_queue.
# Time - O(1) for push and empty, O(n) for pop and top.
# Space - O(n)

from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.appendleft(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        new_queue = deque()
        while True:
            x = self.queue.pop()
            if not self.queue:
                self.queue = new_queue
                return x
            new_queue.appendleft(x)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        new_queue = deque()
        while self.queue:
            x = self.queue.pop()
            new_queue.appendleft(x)
        self.queue = new_queue
        return x

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0