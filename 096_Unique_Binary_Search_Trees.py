_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-binary-search-trees/
# Given an integer n, count all structurally unique BST's (binary search trees) that store values 1...n.

# Dynamic programming.  Base case of 1 for n = 0 or 1.  For each of n possible root nodes, multiply the
# possible left subtrees with the right subtrees.
# Time - O(n**2)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [-1] * (n+1)     # memo[i] is number of ways for i nodes
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n <= 1:
            return 1    # 1 tree for n==0 (empty tree) and 1 tree for n==1

        if memo[n] != -1:
            return memo[n]

        count = 0
        for i in range(1, n+1):     # take each number 1...n as root
            # all numbers < i form left subtree, all > i form right subtree
            # multiply possibilities
            count += self.helper(i-1, memo) * self.helper(n-i, memo)
        memo[n] = count
        return count
