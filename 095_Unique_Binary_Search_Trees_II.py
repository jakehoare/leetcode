_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-binary-search-trees-ii/
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

# Any number i from 1 to n is the root.  Numbers less than i form the left subtree, numbers greater from the right.
# Time - O(n**2 * Catalan(n)) where Catalan(n) = 2n! / (n+1)!n!
# Space - O(n * Catalan(n))

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        return self.generate(1, n)

    def generate(self, left, right):

        if left > right:
            return [None]

        results = []
        for i in range(left, right+1):

            left_trees = self.generate(left, i-1)
            right_trees = self.generate(i+1, right)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    results.append(root)

        return results
