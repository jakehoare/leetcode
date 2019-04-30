_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
# We run a preorder depth first search on the root of a binary tree.
# At each node in this traversal, we output D dashes (where D is the depth of this node),
# then we output the value of this node.
# If the depth of a node is D, the depth of its immediate child is D+1. The depth of the root node is 0.
# If a node has only one child, that child is guaranteed to be the left child.
# Given the output S of this traversal, recover the tree and return its root.

# Recursive helper function takes the required depth for a node to be added (initially zero for the root).
# The depth of the current node is found from the count of "-" and None is returned if this does not match the
# required depth.
# If the depth is as required, the index in S is moved past the "-" and a node is created with the parsed value.
# Add the left and right subtrees by recursing at the next greater depth.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        self.i = 0              # index of next char of S

        def helper(required_depth): # return subtree if root is at required_depth

            depth = 0
            while self.i + depth < len(S) and S[self.i + depth] == "-":
                depth += 1

            if depth != required_depth:
                return None     # self.i is not incremented if depth is not as required

            self.i += depth     # increment self.i
            val = 0
            while self.i < len(S) and S[self.i] != "-":
                val = val * 10 + int(S[self.i])
                self.i += 1
            node = TreeNode(val)

            node.left = helper(required_depth + 1)
            node.right = helper(required_depth + 1)

            return node

        return helper(0)
