_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/subtree-of-another-tree/
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a
# subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.

# Preorder traversal over s and t to serialize. Nodes are separated by commas (e.g. to distinguish 1 and 0 from 10).
# None nodes are identified with special symbol '#'. Check whether serialization of t is contained in s.
# Time - O(m + n)
# Space - O(m + n)

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def serialize(node):
            if not node:
                serial.append("#")
                return
            serial.append(",")
            serial.append(str(node.val))
            serialize(node.left)
            serialize(node.right)

        serial = []         # list so append each symbol in O(1)
        serialize(s)
        s_serial = "".join(serial)
        serial = []
        serialize(t)
        t_serial = "".join(serial)

        return t_serial in s_serial