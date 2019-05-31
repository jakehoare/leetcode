_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized
# to a string and this string can be deserialized to the original tree structure.

# Perform a preorder traversal, appending all visited nodes to a list and special sentinel "null" For None. Recursing
# whenever we see a non-null node. Rebuild by creating a queue and taking the front value.
# Ignore if null, else rebuild the root with value, recurse right then left.
# Time - O(n)
# Space - O(n)

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        nodes = []

        def preorder(node):
            if not node:
                nodes.append("null")
            else:
                nodes.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return ",".join(nodes)  # assumes TreeNode.val do not include comma

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        node_list = deque(data.split(","))

        def rebuild():

            if not node_list:
                return None

            node = node_list.popleft()
            if node == "null":
                return None

            node = TreeNode(node)
            node.left = rebuild()
            node.right = rebuild()
            return node

        return rebuild()