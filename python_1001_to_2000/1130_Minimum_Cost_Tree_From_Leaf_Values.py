_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# Given an array arr of positive integers, consider all binary trees such that:
# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
# Recall that a node is a leaf if and only if it has 0 children.
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and
# right subtree respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.
# It is guaranteed this sum fits into a 32-bit integer.

# Maintain a stack of leaves in descending order. Iterate over the list of leaves.
# While the top of the stack is less than or equal to a leaf, the top of the stack is the smallest leaf.
# Pop off the top of the stack and add to the result the top of stack multiplied by its smallest neighbour,
# (combining the smallest with another leaf). The smallest is no longer used. Add the current leaf to the stack.
# After iterting over leaves, add to the result the product of each remaining pair.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        stack = [float('inf')]          # nodes by descending value

        for a in arr:
            while stack[-1] <= a:
                smallest = stack.pop()
                result += smallest * min(stack[-1], a)
            stack.append(a)

        while len(stack) > 2:           # until root and sentinel
            result += stack.pop() * stack[-1]

        return result
