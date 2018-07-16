_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Breadth-first search. For each level, add all child nodes to new_level and append list of node vals to result.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        level = [root]      # list of nodes in current level

        while level:

            new_level = []
            for node in level:
                new_level += node.children
            result.append([node.val for node in level])
            level = new_level

        return result
