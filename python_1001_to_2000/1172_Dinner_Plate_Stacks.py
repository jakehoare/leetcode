_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/dinner-plate-stacks/
# You have an infinite number of stacks arranged in a row and numbered (left to right) from 0,
# each of the stacks has the same maximum capacity.
# Implement the DinnerPlates class:
# DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
# void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
# int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack,
# and returns -1 if all stacks are empty.
# int popAtStack(int index) returns the value at the top of the stack with the given index and removes it
# from that stack, and returns -1 if the stack with that given index is empty.

# Maintain a list of stacks, where the last stack cannot be empty.
# Also maintain a heap of indices of stacks which are incomplete due to popAtStack(), i.e. not including the last stack.
# Push onto the first available incomplete stack, or the final stack (adding a new one if final stack is at capacity).
# When popping, remove all empty stacks (which may be more than 1 due to popAtStack).
# For popAtStack, use pop if popping from the final stack, else add to the incomplete stacks heap.
# Time - O(n log n) for n operations of push and popAtStack since all existing stacks could be touched. O(n) for pop.
# Space - O(n)

import heapq

class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stacks = []
        self.incomplete_stacks = []     # heap of indices of stacks that have had pop_index

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        while self.incomplete_stacks:   # check or discard all incomplete_stacks in order
            i = heapq.heappop(self.incomplete_stacks)
            if i >= len(self.stacks):
                continue
            self.stacks[i].append(val)
            return

        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])      # start a new stack
        self.stacks[-1].append(val)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        while self.stacks and not self.stacks[-1]:  # discard all empty stacks
            self.stacks.pop()
        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= len(self.stacks) or len(self.stacks[index]) == 0:
            return -1

        if index == len(self.stacks) - 1:           # do not need incomplete_stacks for final stack
            return self.pop()

        heapq.heappush(self.incomplete_stacks, index)
        return self.stacks[index].pop()
