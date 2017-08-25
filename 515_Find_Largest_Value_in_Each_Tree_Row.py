_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# You need to find the largest value in each row of a binary tree.

# BFS. Queue of all nodes by row. Iterate over queue, updating row max and generating next row.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return []
        queue = [root]

        while queue:
            new_queue = []
            max_val = float("-inf")
            for node in queue:
                max_val = max(max_val, node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

            result.append(max_val)
            queue = new_queue

        return result