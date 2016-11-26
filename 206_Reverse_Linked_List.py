_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-linked-list/
# Reverse a singly linked list.

# Iterative resvers.  Alternatively, use recursion.
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed = None
        while head:
            next = head.next
            head.next = reversed
            reversed = head
            head = next
        return reversed