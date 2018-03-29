_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should
# become 1 -> 2 -> 4 after calling your function.

# Copy the value of the next node to the given node and connext the node to the next after next. I.e. remove the next
# node after moving its value to the given node.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next