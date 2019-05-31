_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/serialize-and-deserialize-bst/
# Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be
# serialized to a string and this string can be deserialized to the original tree structure.

# Serialize by preorder traversal. String of values joined by spaces, no None markers.
# Deserialze from deque. If first value is in range, use value as root and recurse left and right subtrees with ranges
# less than and more than value respectively.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


def serialize(self, root):
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    serial_list = []

    def serial(node):
        if not node:
            return
        serial_list.append(str(node.val))
        serial(node.left)
        serial(node.right)

    serial(root)
    return " ".join(serial_list)

def deserialize(self, data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    preorder = deque(int(val) for val in data.split())  # convert to integers

    # if first preorder is between low and high, create tree of all vals in that range with first preorder as root
    def deserial(low, high):
        if preorder and low < preorder[0] < high:
            val = preorder.popleft()
            node = TreeNode(val)
            node.left = deserial(low, val)
            node.right = deserial(val, high)
            return node

    return deserial(float("-inf"), float("inf"))