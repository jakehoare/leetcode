_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Given a binary tree, populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

# Breadth first search by level.
# Time - O(n)
# Space - O(n)

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        level = [root]

        while level and level[0]:   # if first item is None then all are None because perfect, so terminate

            next_level = []
            prev = None

            for node in level:      # set next right pointer
                if prev:
                    prev.next = node
                prev = node

                next_level.append(node.left)    # add nodes to next level list, do not check if None
                next_level.append(node.right)

            level = next_level