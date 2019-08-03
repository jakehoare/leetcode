_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/delete-nodes-and-return-forest/
# Given the root of a binary tree, each node in the tree has a distinct value.
# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).
# Return the roots of the trees in the remaining forest.  You may return the result in any order.

# Recursive helper function returns a node if it is not deleted, else None.
# If a node has no parent and is not deleted, add it to the result list.
# Set the left and right subtrees by recursion.

# Time - O(n)
# Space - O(n)

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete = set(to_delete)      # convert to set for O(1) lookup
        result = []

        def helper(node, has_parent):
            if not node:
                return None
            delete = node.val in to_delete
            if not has_parent and not delete:
                result.append(node)
            node.left = helper(node.left, not delete)
            node.right = helper(node.right, not delete)
            return None if delete else node

        helper(root, False)
        return result
