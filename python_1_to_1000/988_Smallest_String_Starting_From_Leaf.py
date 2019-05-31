_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
# a value of 0 represents 'a', a value of 1 represents 'b', and so on.
# Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically
# smaller than "aba".  A leaf of a node is a node that has no children.

# Bottom-up recursion. Find the results for left and right children. If either or both are the empty string, the
# result is the none empty string concatenated to the node letter. Else return the smallest string plus the node letter.
# The less-than operator "<" finds the smallest string.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):

            if not node:            # base case
                return ""

            node_char = chr(node.val + ord("a"))

            left, right = helper(node.left), helper(node.right)

            if not left or not right:
                return left + right + node_char     # only one of left and right are not ""

            return left + node_char if left < right else right + node_char

        return helper(root)
