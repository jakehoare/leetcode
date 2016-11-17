_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insertion-sort-list/
# Sort a linked list using insertion sort.

# Maintain a sorted part of the list.  For each next node, find its correct location by iterating along sorted section.
# Time - O(n**2)
# Space - O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sorted_tail = dummy = ListNode(float('-inf'))   # sorted_tail is last node of sorted section
        dummy.next = head

        while sorted_tail.next:

            node = sorted_tail.next

            if node.val >= sorted_tail.val:             # node already in correct place
                sorted_tail = sorted_tail.next
                continue

            sorted_tail.next = sorted_tail.next.next    # cut out node

            insertion = dummy
            while insertion.next.val <= node.val:
                insertion = insertion.next

            node.next = insertion.next                  # put node after insertion
            insertion.next = node

        return dummy.next

