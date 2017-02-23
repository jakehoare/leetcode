_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# You are given an integer array nums and you have to return a new counts array. The counts array has the property
# where counts[i] is the number of smaller elements to the right of nums[i].

# Create a binary search tree that tracks the number of smaller entries in left subtree of each node.  For each
# num in array starting from right, find number of smaller entries in BST and simultaneously add node.
# Time - O(n*n), n log n if balanced
# Space - O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.smaller = 0    # number of entries in left subtree
        self.left = None
        self.right = None

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = [0 for _ in range(len(nums))]
        if len(nums) < 2:
            return smaller
        root = TreeNode(nums[-1])

        for i in range(len(nums)-2, -1, -1):    # left to right
            node = root
            count = 0                           # nb entries smaller than nums[i]

            while True:
                if nums[i] < node.val:
                    node.smaller += 1           # increment left subtree count and move left
                    if not node.left:
                        node.left = TreeNode(nums[i])
                        break
                    else:
                        node = node.left

                else:   # nums[i] >= node.val
                    count += node.smaller       # all nodes in left subtree
                    if nums[i] > node.val:      # and this node if node.val != nums[i]
                        count += 1
                    if not node.right:
                        node.right = TreeNode(nums[i])
                        break
                    else:
                        node = node.right

            smaller[i] = count

        return smaller