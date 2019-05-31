_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

# Heap stores k closest values as tuples (- abs node diff from target, node value).  Top of heap is furthest from
# target.  If a node.val is closer than the furthest value in the heap then add it to the heap and check left and
# right subtrees.  If a node.val is further than the furthest value in the heap then the nodes of one subtree are all
# also further away.
# Alternatively, preorder traverse tree to create a sorted list.  Find the pair of values surrounding target and
# expand outwards always taking the closest to target. O(n + k) but always visits ever node.
# Time - O(n log k)
# Space - O(k)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import heapq

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        closest = [(float('-inf'), 0)]      # add one item to avoid checking for empty heap
        self.find_closest(root, target, k, closest)
        return [val for _, val in closest]

    def find_closest(self, node, target, k, closest):
        if not node:
            return

        if abs(node.val - target) < -closest[0][0]:     # node.val is closer to target than furthest in heap
            heapq.heappush(closest, (-abs(node.val - target), node.val))
            if len(closest) > k:                        # heap is over capacity
                heapq.heappop(closest)
            self.find_closest(node.left, target, k, closest)
            self.find_closest(node.right, target, k, closest)

        elif target > node.val:     # LHS nodes cannot be closer than node.val, which is itself not in k closest
            self.find_closest(node.right, target, k, closest)
        else:
            self.find_closest(node.left, target, k, closest)