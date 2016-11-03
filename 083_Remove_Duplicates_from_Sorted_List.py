_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# If next node is same as node, link node to node.next.next. Else move to next node.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head

        while node and node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head
