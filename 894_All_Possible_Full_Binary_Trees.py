_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/all-possible-full-binary-trees/
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.
# Return a list of all possible full binary trees with N nodes.
# Each element of the answer is the root node of one possible tree.
# Each node of each tree in the answer must have node.val = 0.
# You may return the final list of trees in any order.

# If N is even we cannot build a full tree. To build a tree of size N, create a root and for each odd sized left
# subtree, build all possible left and right subtrees. Combine the left and right subtrees in all possible ways.
# Memoize intermediate results to avoid repetition.
# Time - O(2**n)
# Space - O(2**n)

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        memo = {}

        def helper(n):

            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]

            result = []

            for left_size in range(1, n, 2):

                right_size = n - 1 - left_size
                left_subtrees = helper(left_size)
                right_subtrees = helper(right_size)

                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(0)
                        root.left = left_subtree
                        root.right = right_subtree
                        result.append(root)

            memo[n] = result
            return result

        return helper(N)