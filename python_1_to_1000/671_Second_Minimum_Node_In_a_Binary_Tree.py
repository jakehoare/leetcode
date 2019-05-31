_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree
# has exactly two or zero sub-node.
# If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.
# Given such a binary tree, output the second minimum value in the set made of all the nodes' value in the whole tree.
# If no such second minimum value exists, output -1 instead.

# The root value is the minimum value, since all children are >= root value. Second minimum must be a child of a node
# with the minimum (root) value. If a node has the root value then recursively check its children.
# Else it has a larger value, so update second_min.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min_val = root.val  # assumes root exists
        self.second_min = float("inf")

        def helper(node):

            if not node:
                return

            if node.val == min_val:
                helper(node.left)
                helper(node.right)
            else:  # node.val > min_val
                self.second_min = min(node.val, self.second_min)

        helper(root)

        return -1 if self.second_min == float("inf") else self.second_min