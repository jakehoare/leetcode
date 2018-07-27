_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/quad-tree-intersection/
# A quadtree is a tree data in which each internal node has exactly four children: topLeft, topRight, bottomLeft
# and bottomRight. Quad trees are often used to partition a two-dimensional space by recursively subdividing it into
# four quadrants or regions.
# We want to store True/False information in our quad tree.
# The quad tree is used to represent a N * N boolean grid. For each node, it will be subdivided into four children
# nodes until the values in the region it represents are all the same. Each node has another two boolean
# attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node.
# The val attribute for a leaf node contains the value of the region it represents.

# Information required but not in problem description: the val attribute for a non-leaf node is False.
# Combine two leaves according the logical OR of their values. If one node is a leaf then return it if is True, else
# return the other node. If neither are leaves, intersect each of the 4 subtree children and return a leaf if they are
# all leaves with the same value, or else return a non-leaf with value of False.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1

        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        children = [topLeft, topRight, bottomLeft, bottomRight]
        values = [child.val for child in children]
        leaves = [child.isLeaf for child in children]

        if all(leaves) and (sum(values) == 0 or sum(values) == 4):
            return Node(topLeft.val, True, None, None, None, None)

        # non-leaf must have False val
        return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)