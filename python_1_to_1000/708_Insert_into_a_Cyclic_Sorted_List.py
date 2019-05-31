_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/
# Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into
# the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list,
# and may not be necessarily the smallest value in the cyclic list.
# If there are multiple suitable places for insertion, you may choose any place to insert the new value.
# After the insertion, the cyclic list should remain sorted.
# If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference
# to that single node. Otherwise, you should return the original given node.

# Iterate along the list handling 3 cases,
# 1) Increasing node values - insert if insertVal is between (inclusive) node and node.next
# 2) Decreasing node values - insert if insertVal is >= node.val or <= node.next.val, i.e. beyond the range
# 3) Same node values - insert if revisiting start, since all nodes have the same value
# Time - O(n)
# Space - O(1)

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:                            # list is empty, return node referencing itself
            new_node = Node(insertVal, None)
            new_node.next = new_node
            return new_node

        def insert_after(node):
            node.next = Node(insertVal, node.next)

        original_head = head                    # save so can be returned and can tell if full cycle traversed

        while True:

            if head.next.val > head.val:        # next node is increasing
                if insertVal >= head.val and insertVal <= head.next.val:    # check if insertVal between node vals
                    break
            elif head.next.val < head.val:      # next node is decreasing
                if insertVal >= head.val or insertVal <= head.next.val:     # check if insertVal beyond range of cycles
                    break
            elif head.next == original_head:                                # all nodes same value , insert anywhere
                break

            head = head.next

        insert_after(head)
        return (original_head)
