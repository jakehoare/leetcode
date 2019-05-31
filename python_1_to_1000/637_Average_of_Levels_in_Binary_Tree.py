_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

# Breadth first search. Maintain a queue of nodes in the current level.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes = [root]
        result = []

        while True:

            row_sum, row_count = 0, 0       # no need to use a list to store the values
            new_nodes = []

            for node in nodes:
                if not node:                # ignore None
                    continue
                row_sum += node.val
                row_count += 1
                new_nodes.append(node.left) # add children to next queue
                new_nodes.append(node.right)

            if row_count == 0:
                break
            result.append(row_sum / float(row_count))
            nodes = new_nodes               # check next row even if all nodes are None

        return result