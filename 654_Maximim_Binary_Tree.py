_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-binary-tree/
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.

# For each array, find the maximum and set to root, then recurse for left and right subtrees.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(i, j):   # construct subtree from nums[i:j + 1]
            if i > j:
                return None

            max_num = float("-inf")
            for k in range(i, j + 1):
                if nums[k] > max_num:
                    max_num = nums[k]
                    max_index = k

            root = TreeNode(max_num)
            root.left = helper(i, max_index - 1)
            root.right = helper(max_index + 1, j)

            return root

        return helper(0, len(nums) - 1)