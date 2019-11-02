_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Maintain a min heap of tuples of (val, node) for the next node in each list.
# Time - O(n log k) for n total nodes, each of which is pushed and popped from heap in log k time.
# Space - O(k) for heap of k nodes

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        prev = dummy = ListNode(None)

        next_nodes = [(l.val, l) for l in lists if l]
        heapq.heapify(next_nodes)

        while next_nodes:
            value, node = heapq.heappop(next_nodes)
            prev.next = node
            prev = prev.next
            if node.next:
                heapq.heappush(next_nodes, (node.next.val, node.next))

        return dummy.next
