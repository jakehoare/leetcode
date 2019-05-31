_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# We are given a binary tree (with root node root), a target node, and an integer value K.
# Return a list of the values of all nodes that have a distance K from the target node.
# The answer can be returned in any order.

# Depth-first search until target is found. From target, add to results all nodes in subtree rooted at target that
# are at distance K. If target is in a subtree, if distance to target == K then ad this node to results, else if
# distance to target is less than K then explore the subtree that does not contain target, adding to results all nodes
# that are total distance K form target.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        results = []

        def nodes_at_distance(node, distance):      # update results for all subtree nodes at distance from node

            if not node:
                return
            if distance == 0:
                results.append(node.val)
            else:
                nodes_at_distance(node.left, distance - 1)
                nodes_at_distance(node.right, distance - 1)

        def helper(node):                           # returns distance to target in this subtree or -1 if no target

            if not node:
                return -1

            if node == target:
                nodes_at_distance(node, K)          # add to results all nodes at distance K in this subtree
                return 0

            left, right = helper(node.left), helper(node.right)
            if left == -1 and right == -1:          # target is in neither subtree
                return -1
            distance_to_target = 1 + max(left, right)   # target is in a subtree

            if K - distance_to_target == 0:         # add this node to results
                nodes_at_distance(node, 0)
            elif K - distance_to_target > 0:        # find nodes on other_side that are K from target
                other_side = node.left if left == -1 else node.right
                nodes_at_distance(other_side, K - distance_to_target - 1)

            return distance_to_target

        helper(root)
        return results