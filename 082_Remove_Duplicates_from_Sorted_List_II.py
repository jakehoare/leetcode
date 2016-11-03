_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# If node is duplicated, move past all nodes of same value.  Else add node to final list.
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
        pseudo = prev = ListNode(None)
        pseudo.next = head
        node = head

        while node:

            if node.next and node.val == node.next.val:     # node begins a sequence of duplicates
                duplicate_value = node.val
                node = node.next
                while node and node.val == duplicate_value: # skip over all duplicates
                    node = node.next
                prev.next = None                            # list ends until non-duplicate found

            else:                   # node is not duplicated
                prev.next = node    # add to resulting list
                prev = node
                node = node.next

        return pseudo.next
