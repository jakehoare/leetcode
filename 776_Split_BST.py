_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-bst/
# Given a Binary Search Tree (BST) with root node root, and a target value V, split the tree into two subtrees where
# one subtree has nodes that are all smaller or equal to the target value, while the other subtree has all nodes that
# are greater than the target value.  It's not necessarily the case that the tree contains a node with value V.
# Additionally, most of the structure of the original tree should remain.
# Formally, for any child C with parent P in the original tree, if they are both in the same subtree after the split,
# then node C should still have the parent P.
# You should output the root TreeNode of both subtrees after splitting, in any order.

# Helper function recursively splits BST into a tree with nodes <= V and a tree with nodes > V. One side is always
# unchanged and the recursion splits the other side into 2 parst, one of which is added back as a new left or right
# subtree.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        def splitter(node):

            if not node:
                return [None, None]

            if V < node.val:
                less, more = splitter(node.left)    # recurse left, node.right is unchanged
                node.left = more                    # new left is the tree with nodes > V
                return [less, node]

            less, more = splitter(node.right)       # recurse right, node.left is unchanged if V == node.val
            node.right = less
            return [node, more]

        return splitter(root)