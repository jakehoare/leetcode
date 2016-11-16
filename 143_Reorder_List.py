_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reorder-list/
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,  reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# Do this in-place without altering the nodes' values.

# Find the mid point, reverse list after mid point, then interleave the 2 sides.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        # set slow to mid for odd length lists, first of second half for even
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse nodes after slow (slow has pointers from both sides)
        prev, node = None, slow
        while node:
            prev, node.next, node = node, prev, node.next

        first, second = head, prev  # heads of the normal and reversed lists
        while second.next:
            first.next, first = second, first.next      # insert second after first
            second.next, second = first, second.next    # insert first after second

