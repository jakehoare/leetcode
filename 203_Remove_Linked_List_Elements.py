_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-linked-list-elements/
# Remove all elements from a linked list of integers that have value val.

# Iterate along list, cutting out nodes with val.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(None)   # dummy in case head is deleted
        dummy.next = head

        while head:

            if head.val == val:
                prev.next, head.next, head = head.next, None, head.next
            else:
                prev, head = head, head.next

        return dummy.next