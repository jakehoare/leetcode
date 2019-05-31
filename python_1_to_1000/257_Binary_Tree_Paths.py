_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-paths/
# Given a binary tree, return all root-to-leaf paths.

# Recursive dfs. If leaf, add path to result. Else add node value to partial and recurse.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def helper(node, partial):          # partial is exiting path from root
            if not node:
                return
            partial.append(str(node.val))
            if not node.left and not node.right:
                paths.append("->".join(partial))
                return
            helper(node.left, partial[:])
            helper(node.right, partial)

        paths = []
        helper(root, [])
        return paths
