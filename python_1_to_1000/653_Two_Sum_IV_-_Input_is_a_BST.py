_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their
# sum is equal to the given target.

# Traverse the BST. Preorder is used but could be postorder or inorder. For each node, check if k - node.val has
# already been visited. If node, add noe.val to the visited set. Would work equally well for a binary tree that is not
# a BST.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        visited = set()

        def traverse(node):

            if not node:
                return False

            if k - node.val in visited:
                return True
            visited.add(node.val)

            return traverse(node.left) or traverse(node.right)

        return traverse(root)