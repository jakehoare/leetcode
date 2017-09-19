_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
# Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.
# Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered
# valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where
# not necessarily be parent-child order.

# Helper return longest increasing and decreasing paths from a node. Update longest increasing and decreasing paths
# according to whether children exist and their values are +/-1 of node.val. Update longest path without double-
# counting node.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0    # instance variable to store longest path length

        def helper(node):   # return tuple (longest increasing, longest decreasing) (including node)
            if not node:
                return 0, 0

            l_i, l_d = helper(node.left)
            r_i, r_d = helper(node.right)

            incr, decr = 1, 1   # leaf node

            if node.left:
                if node.left.val == node.val + 1:   # increasing path
                    incr = 1 + l_i
                elif node.left.val == node.val - 1: # decreasing path
                    decr = 1 + l_d

            if node.right:
                if node.right.val == node.val + 1:
                    incr = max(incr, 1 + r_i)       # update best increasing
                elif node.right.val == node.val - 1:
                    decr = max(decr, 1 + r_d)       # update best decreasing

            self.longest = max(self.longest, incr + decr - 1)   # -1 so as to not double count node

            return incr, decr

        helper(root)
        return self.longest