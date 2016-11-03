_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/partition-list/
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.

# Create new pseudo heads for lists of nodes lesser and greater than x.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lesser_head = lesser = ListNode(None)
        greater_head = greater = ListNode(None)

        node = head
        while node:
            if node.val < x:
                lesser.next = node
                lesser = node
            else:                       # node.val >= x
                greater.next = node
                greater = node
            node = node.next

        greater.next = None                 # if last node not greater then break link to last node
        lesser.next = greater_head.next     # join lists
        return lesser_head.next