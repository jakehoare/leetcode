_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-univalue-subtrees/
# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.

# Bottom-up count univariate subtrees in left and right subtrees than add 1 if both subtrees are univariate with the
# same value as the root.
# Alternatively define a function to test if the subtree rooted at that node is univariate (which explores the subtree)
# and preorder (or inorder/postorder) traverse the tree to test all nodes.  O(n**2) time but runs faster on the
# leetcode test cases.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.univariates = 0
        self.is_univariate(root)
        return self.univariates

    # returns True if tree from root is univariate and increments count for all univariate subtrees
    def is_univariate(self, root):

        if not root:
            return True

        left_uni = self.is_univariate(root.left)
        right_uni = self.is_univariate(root.right)

        if left_uni and right_uni:
            if (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
                self.univariates += 1
                return True

        return False



class Solution2(object):
    def countUnivalSubtrees(self, root):
        self.univariates = 0
        self.preorder(root)
        return self.univariates

    def preorder(self, root):
        if not root:
            return
        if self.is_univariate(root):
            self.univariates += 1
        self.preorder(root.left)
        self.preorder(root.right)

    def is_univariate(self, root):
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.is_univariate(root.left) and self.is_univariate(root.right)
