_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-sum-iii/
# You are given a binary tree in which each node contains an integer value.
# Find the number of paths that sum to a given value.
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent
# nodes to child nodes).

# Maintain dictionary counting the paths from root to current node. Visit each node and count the paths ending at that
# node with target sum. Increment the count of the path to the node in the dictionary and recurse left and right.
# Decremetn count after recursion.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        paths = defaultdict(int)    # key is sum of path from root, value is the count of such paths
        paths[0] = 1                # one path has zero sum

        def helper(node, partial):

            if not node:
                return 0

            partial += node.val
            count = paths[partial - sum]    # paths ending at node

            paths[partial] += 1
            count += helper(node.left, partial)
            count += helper(node.right, partial)
            paths[partial] -= 1

            return count

        return helper(root, 0)