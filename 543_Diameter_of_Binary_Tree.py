_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/diameter-of-binary-tree/
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.

# Bottom up recursion. The longest path passing with a node as root is the longest downwards left path + longest
# downwards right path.
# If there is no child on right or left then the longest path on that side is zero. Else longest path is 1 + longest
# of left and right paths down from child.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.diameter = 0

        def helper(node):       # return (longest path down left, longest path down right)

            left_longest = 0 if not node.left else 1 + max(helper(node.left))
            right_longest = 0 if not node.right else 1 + max(helper(node.right))

            self.diameter = max(self.diameter, left_longest + right_longest)    # update overall longest path
            return (left_longest, right_longest)

        helper(root)            # ignore return value
        return self.diameter