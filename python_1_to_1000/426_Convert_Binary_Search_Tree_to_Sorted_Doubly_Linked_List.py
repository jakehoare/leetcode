_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# Convert a BST to a sorted circular doubly-linked list in-place.
# Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
# Each node in a doubly linked list has a predecessor and successor.
# For a circular doubly linked list, the predecessor of the first element is the last element,
# and the successor of the last element is the first element.

# Recursively convert left and right subtrees to circular linked lists. Link tail of left subtree to root and head of
# right subtree to root. Complete the circle by linking head and tail.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)

        if left_head:
            root.left = left_head.left      # link root to tail of left subtree
            left_head.left.right = root
        else:
            left_head = root                # no subtree on left, root is left_head

        if right_head:
            root.right = right_head         # link root to head of right_subtree
            right_tail = right_head.left    # store right_tail
            right_head.left = root
        else:
            right_tail = root               # no subtree on right, root is right_tail

        left_head.left = right_tail         # link head and tail
        right_tail.right = left_head

        return left_head