_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Given two binary search trees root1 and root2.
# Return a list containing all the integers from both trees sorted in ascending order.

# Perform inorder traversals on each tree to get the node in ascending value order.
# Then iterate along the sorted lists to merge them.
# Alternatively, sort tree1 and tree2 instead of merging.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder(node, ascending):
            if not node:
                return
            inorder(node.left, ascending)
            ascending.append(node.val)
            inorder(node.right, ascending)

        tree1, tree2 = [], []
        inorder(root1, tree1)
        inorder(root2, tree2)

        result = []
        i, j = 0, 0                                 # indices of next elements to merge
        while i < len(tree1) and j < len(tree2):    # until one list is exhausted
            if tree1[i] <= tree2[j]:
                result.append(tree1[i])
                i += 1
            else:
                result.append(tree2[j])
                j += 1

        return result + tree1[i:] + tree2[j:]       # append remaining nodes
