_author_ = 'jake'
_project_ = 'leetcode'


# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Count the length of the list.  Form left subtree from nodes before mid.  Mid node forms root, then right subtree
# from nodes after mid.  When a new tree node is made, advance the linked list pointer.  Bottom-up approach.
# Time - O(n)
# Space - O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        return self.list_to_bst([head], 0, count - 1)   # [head] is mutable list of next list node to be converted


    def list_to_bst(self, node_as_list, start, end):  # convert linked-list nodes from start to end (inclusive)

        if start > end:
            return None

        mid = (start + end) // 2

        left_subtree = self.list_to_bst(node_as_list, start, mid - 1)   # will update contents of node_as_list to
                                                                        # become the mid node of linked list
        root = TreeNode(node_as_list[0].val)
        root.left = left_subtree
        node_as_list[0] = node_as_list[0].next      # update entry to next node of linked-list

        root.right = self.list_to_bst(node_as_list, mid + 1, end)

        return root

