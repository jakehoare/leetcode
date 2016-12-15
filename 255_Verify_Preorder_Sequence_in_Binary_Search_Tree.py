_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
# You may assume each number in the sequence is unique.

# Whilst the values are decreasing they are left children and we push them onto a stack.  When we see a higher value
# it must be a right child so pop off all smaller values, the last of which is the parent of the current value.
# Anything smaller than the parent should have been traversed already so parent is the minimum of future values.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = [float('inf')]      # added so do not need to check is empty
        minimum = float('-inf')

        for value in preorder:

            if value < minimum:
                return False

            while value > stack[-1]:
                minimum = stack.pop()   # will only ever increase
            stack.append(value)

        return True