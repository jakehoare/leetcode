_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-pruning/
# We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# Recall that the subtree of a node X is X, plus every node that is a descendant of X.

# Recursive helper function returns boolean whether tree has a node with val == 1 and also removes subtrees not
# containing 1.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def contains_one(node):

            if not node:
                return False
            left_one, right_one = contains_one(node.left), contains_one(node.right) # explore and prune children

            if not left_one:                                # remove subtrees without 1s
                node.left = None
            if not right_one:
                node.right = None

            return node.val == 1 or left_one or right_one   # 1 in node or subtrees

        return root if contains_one(root) else None         # handle tree with no 1s