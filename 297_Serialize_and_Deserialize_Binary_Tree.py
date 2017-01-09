_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
# to a string and this string can be deserialized to the original tree structure.

# Perform a preorder traversal, recursing whenever we see a non-null node.  Rebuild by creating a queue and taking
# thr front value.  Ignore if null, else rebuild the root with value, recur right then left.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        encoding = []
        self.preorder(root, encoding)
        return ",".join(encoding)           # assumes TreeNode.val do not include comma

    def preorder(self, node, encoding):
        if not node:
            encoding.append("null")
        else:
            encoding.append(str(node.val))
            self.preorder(node.left, encoding)
            self.preorder(node.right, encoding)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        return self.rebuild(deque(data.split(",")))

    def rebuild(self, node_list):

        if not node_list:
            return None

        node = node_list.popleft()
        if node == "null":
            return None

        node = TreeNode(node)
        node.left = self.rebuild(node_list)
        node.right = self.rebuild(node_list)
        return node