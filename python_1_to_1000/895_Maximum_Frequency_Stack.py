_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-frequency-stack/
# Implement FreqStack, a class which simulates the operation of a stack-like data structure.
# FreqStack has two functions:
# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the stack.
# If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

# Maintain a dictionary counting the number of each element in the stack and a stack_of_stacks. stack_of_stacks
# contains stacks of elements grouped by their counts. push() an element to the stack according to its count.
# pop() an element from the top stack_of_stacks.
# Time - O(1) for all methods
# Space - O(n)

from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        self.counter = defaultdict(int)     # count of each element in stack
        self.stack_of_stacks = []           # stack_of_stacks[i] is stack of elelemts with count of i + 1

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.counter[x] += 1
        count = self.counter[x]

        if count > len(self.stack_of_stacks):   # new stack
            self.stack_of_stacks.append([])
        self.stack_of_stacks[count - 1].append(x)

    def pop(self):
        """
        :rtype: int
        """
        num = self.stack_of_stacks[-1].pop()    # pop from highest count stack
        self.counter[num] -= 1

        if not self.stack_of_stacks[-1]:        # remove empty highest stack
            self.stack_of_stacks.pop()

        return num