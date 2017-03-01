_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the
# node's value. If it is a null node, we record a sentinel value such as #.  Given a string of comma separated values,
# verify whether it is a correct preorder traversal serialization of a binary tree.

# The number of leaves = number of internal nodes + 1.  Count the number of future leaves based upon the internal
# nodes seen.  If this is zero and there are other nodes left then we already have a complete tree and there can be
# no more nodes.  Likewise if there are any expected leaves remaining after parsing the tree it is not complete.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        expected_leaves = 1

        for node in preorder.split(","):
            if expected_leaves == 0:
                return False
            if node == "#":
                expected_leaves -= 1
            else:
                expected_leaves += 1

        return expected_leaves == 0