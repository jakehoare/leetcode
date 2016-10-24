_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given a linked list, remove the nth node from the end of list and return its head.

# Advance first pointer n steps then advance both pointers at same rate.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first, second = head, head

        for i in range(n):      # move first n steps forwards
            first = first.next
        if not first:
            return head.next

        while first.next:       # move both pointers until first is at end
            first = first.next
            second = second.next
        second.next = second.next.next  # nth from end is second.next
        return head