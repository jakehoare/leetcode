_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# Given a binary tree with the following rules:
# root.val == 0
# If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
# If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
# Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.
# You need to first recover the binary tree and then implement the FindElements class:
# FindElements(TreeNode* root) Initializes the object with a canotaminated binary tree, you need to recover it first.
# bool find(int target) Return if the target value exists in the recovered binary tree.

# Recursively explore the tree by depth-first search, adding all values to a set.
# Then lookup each value.
# Time - O(n) for __init__ and O(1) for find
# Space - O(n)

class FindElements(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.elements = set()

        def helper(node, val):      # explore tree from node with correct value val
            if not node:
                return
            self.elements.add(val)
            helper(node.left, 2 * val + 1)
            helper(node.right, 2 * val + 2)

        helper(root, 0)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.elements