_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# Given the head of a linked list,
# we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.

# Iterate along the list, updating a running sum of node values.
# If we have running sum that has been seen before, connect the previous node with the running sum to the next node,
# thereby removing the zero sum sequence from the list.
# Use an OrderedDict so we can pop all the eliminated nodes off the dictionary.
# Alternatively, when a zero sum sequence is found eliminate those nodes and start from the head again.
# So the dictionary does not have to be cleared.
# Time - O(n)
# Space - O(n)

from collections import OrderedDict

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)             # create a new dummy head, in case the head is removed
        dummy.next = head
        node = dummy
        running_sum = 0                 # sum of all node vals seen
        sum_to_node = OrderedDict()     # map running_sum to ListNode

        while node:
            running_sum += node.val
            to_connect = sum_to_node.get(running_sum, node)     # node to be connected to node.next

            while running_sum in sum_to_node:                   # remove eliminated nodes
                sum_to_node.popitem()
            sum_to_node[running_sum] = to_connect

            node = to_connect.next = node.next

        return dummy.next
