_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-circular-queue/
# Design your implementation of the circular queue. The circular queue is a linear data structure in which the
# operations are performed based on FIFO (First In First Out) principle and the last position is connected back to
# the first position to make a circle. It is also called "Ring Buffer".
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front
# of the queue. But using the circular queue, we can use the space to store new values.
# Your implementation should support following operations:
#
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.

# Use a python list as a circular array. Add an extra space, which allows us to distinguish between empty and full
# queues.
# Time - O(1)
# Space - O(n)

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k + 1              # always have one space to separate head from tail
        self.q = [None] * self.k
        self.head = self.tail = 0   # tail is always empty

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail - 1) % self.k
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head = (self.head - 1) % self.k  # just move head, no need to delete element
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[(self.tail + 1) % self.k]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.head == self.tail

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return (self.head + 1) % self.k == self.tail