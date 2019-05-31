_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/max-stack/
# Design a max stack that supports push, pop, top, peekMax and popMax.
#  push(x) -- Push element x onto stack.
#  pop() -- Remove the element on top of the stack and return it.
#  top() -- Get the element on the top.
#  peekMax() -- Retrieve the maximum element in the stack.
#  popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements,
#    only remove the top-most one.

# Stack contains tuples of (element, max element in stack). To popMax, pop until an element equal to max is seen. Then
# push back all elements before max in reverse order.
# Time - O(1) for all operations apart from O(n) for popMax
# Space - O(n)

class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [(float("-inf"), float("-inf"))]  # pairs of (num, max_num)

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: int
        """
        x, _ = self.stack.pop()
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        temp = []
        x, target = self.stack.pop()

        while x != target:
            temp.append(x)
            x, _ = self.stack.pop()

        for x in reversed(temp):
            self.push(x)

        return target