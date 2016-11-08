_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Create a list of all non-null nodes from the nodes in the level above.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result

        level_nodes = [root]

        while level_nodes:

            new_level_nodes = []
            result.append([])

            for node in level_nodes:
                result[-1].append(node.val)
                if node.left:
                    new_level_nodes.append(node.left)
                if node.right:
                    new_level_nodes.append(node.right)

            level_nodes = new_level_nodes

        return result
