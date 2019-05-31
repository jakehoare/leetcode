_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Mid element is root, recursively form left and right subtrees.
# Time - O(n)
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.convert(nums, 0, len(nums)-1)

    def convert(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.convert(nums, left, mid-1)
        root.right = self.convert(nums, mid+1, right)
        return root
