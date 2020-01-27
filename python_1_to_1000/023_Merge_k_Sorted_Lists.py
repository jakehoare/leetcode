_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/merge-k-sorted-lists/
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Maintain a min heap of tuples of (val, list index) for the next node in each list.
# Also maintain a list of the next node to be merged for each list index.
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
        next_nodes, heap = [], []

        for i, node in enumerate(lists):
            next_nodes.append(node)         # next_nodes[i] is the next node to be merged from lists[i]
            if node:
                heap.append((node.val, i))
        heapq.heapify(heap)

        while heap:
            value, i = heapq.heappop(heap)
            node = next_nodes[i]
            prev.next = node                # add node to merged list
            prev = prev.next
            if node.next:
                next_nodes[i] = node.next
                heapq.heappush(heap, (node.next.val, i))

        return dummy.next
