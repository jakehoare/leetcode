_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# Return any binary tree that matches the given preorder and postorder traversals.
# Values in the traversals pre and post are distinct positive integers.

# The root is the first node of pre and the last node of post. The penultimate node of post is the root of the right
# subtree of root. Find this right root in pre. All nodes before it in pre form the left subtree and all after and
# including form the right subtree. The nodes in post that form the left subtree are deduced from the length of the
# sile of pre that forms the left subtree. A mapping of pre from value to index ensures finding a node is O(1).
# Time - O(n)
# Space - O(n)

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def helper(pre_start, pre_end, post_start, post_end):   # build subtree using pre[pre_start:pre_end]
                                                                # and post[post_start, post_end]
            if pre_start == pre_end:
                return None

            root = TreeNode(pre[pre_start])
            if post_end == post_start + 1:
                return root

            idx = pre_indices[post[post_end - 2]]       # index of root of right subtree in pre
            left_size = idx - pre_start - 1             # number of nodes in left subtree
            root.left = helper(pre_start + 1, idx, post_start, post_start + left_size)
            root.right = helper(idx, pre_end, post_start + left_size, post_end - 1)

            return root

        pre_indices = {val: i for i, val in enumerate(pre)} # map from node value to index in pre
        return helper(0, len(pre), 0, len(post))