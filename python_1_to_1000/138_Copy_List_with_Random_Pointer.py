_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/copy-list-with-random-pointer/
# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.

# Duplicate every node and insert copy in list after original node.  Link copied nodes to random pointers, which
# follow random pointers of original nodes.  Separate out original and copied lists.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node = head
        while node:
            next = node.next
            copy = RandomListNode(node.label)
            node.next = copy
            copy.next = next
            node = next

        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        pseudo = prev = RandomListNode(0)
        node = head
        while node:
            prev.next = node.next
            node.next = node.next.next
            node = node.next
            prev = prev.next

        return pseudo.next