_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/linked-list-random-node/
# Given a singly linked list, return a random node's value from the linked list. Each node must have the same
# probability of being chosen.

# Count length and move along a random number of nodes.  Alternatively if getRandom() is called many times, store
# vals in a list and choose a random index (O(n) space and O(1) getRandom).
# Alternatively, reservoir sampling.  Choose first item, for each subsequent ith item, replace chosen with ith with
# probability 1/(1+i).  Slow due to multiple random samples.
# Time - O(n)
# Space - O(1)

import random

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.count = 0
        while head:
            self.count += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        randnode = random.randint(0, self.count - 1)
        node = self.head
        for _ in range(randnode):
            node = node.next
        return node.val
