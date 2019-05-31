_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution still work?

# Breadth first search by level. Only append non-null nodes to level list.
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
        if not root:
            return
        level = [root]

        while level:
            next_level = []
            prev = None
            for node in level:
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level
