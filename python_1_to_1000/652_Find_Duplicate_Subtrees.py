_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-duplicate-subtrees/
# Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return
# the root node of any one of them.
# Two trees are duplicate if they have the same structure with same node values.

# Preorder traversal. Create a string representation of each subtree and map that string to a list of root nodes.
# Time - O(n**2)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def serialize(node):
            if not node:
                return "#"
            serial = str(node.val) + "," + serialize(node.left) + "," + serialize(node.right)
            subtrees[serial].append(node)
            return serial

        subtrees = defaultdict(list)    # key is serialised subtree, value is list of subtree nodes
        serialize(root)                 # ignore return value
        return [nodes[0] for serial, nodes in subtrees.items() if len(nodes) > 1]