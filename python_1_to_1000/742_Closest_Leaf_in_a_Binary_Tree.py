_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/
# Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node
# to target k in the tree. Here, nearest to a leaf means the least number of edges travelled on the binary tree to
# reach any leaf of the tree. Also, a node is called a leaf if it has no children.
# There exists some node in the given binary tree for which node.val == k.

# Bottom-up recursion through the tree to find the closest leaf to every node when moving downwards to subtrees.
# The recurse through the tree again, updating closest leaves for cases that best path is via parent.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nearest_leaves = {0: (float("inf"), 0)} # key is node.val, value is (distance to leaf, leaf.val)

        def closest_down(node):                 # create mapping for closes leaf node via subtrees

            if not node:
                return (float("inf"), 0)

            if not node.left and not node.right:    # node is a leaf
                result = (0, node.val)
            else:
                left_dist, left_nearest = closest_down(node.left)
                right_dist, right_nearest = closest_down(node.right)
                if left_dist <= right_dist:     # closest leaf is via left subtree
                    result = (left_dist + 1, left_nearest)
                else:
                    result = (right_dist + 1, right_nearest)

            nearest_leaves[node.val] = result
            return result

        def closest(node, parent_val):          # update the mapping for nodes with closer leaves via parents

            if not node:
                return

            if 1 + nearest_leaves[parent_val][0] < nearest_leaves[node.val][0]:     # closer leaf via parent
                nearest_leaves[node.val] = (1 + nearest_leaves[parent_val][0], nearest_leaves[parent_val][1])

            closest(node.left, node.val)
            closest(node.right, node.val)

        closest_down(root)
        closest(root, 0)
        return nearest_leaves[k][1]