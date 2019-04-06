_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/next-greater-node-in-linked-list/
# We are given a linked list with head as the first node.
# Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
# Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i,
# node_j.val > node_i.val, and j is the smallest possible choice.
# If such a j does not exist, the next larger value is 0.
# Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

# Iterate along the list, maintaining a stack of nodes without greater elements. Stack contains nodes in descending
# order (otherwise next greater value would be known), and node indices.
# For each node, pop all smaller values off the stack and update their next greater values with the
# current node value.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        result = []
        stack = []              # (index, val) tuples of nodes without next greater, ordered by decreasing val
        node = head
        i = 0                   # index of node in list

        while node:

            result.append(0)    # add a new entry to result with default of 0 if no greater node

            while stack and stack[-1][1] < node.val:  # all smaller vals have the current node as the next greater
                j, _ = stack.pop()
                result[j] = node.val

            stack.append((i, node.val))
            i += 1
            node = node.next

        return result
