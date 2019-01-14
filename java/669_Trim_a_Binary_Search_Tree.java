/*
https://leetcode.com/problems/trim-a-binary-search-tree/
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements
lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of
the trimmed binary search tree.

If a node has val between L and R (inclusive) then return recurively update the subtrees and return the node.
If a node is less than L then only its right subtree can contain values in the requires range. Similarly a node
with val greater than R can only have values in its left subtree in the range.
Time - O(n)
Space - O(1)
*/

class Solution {
    public TreeNode trimBST(TreeNode root, int L, int R) {

        if (root == null)
            return null;

        if (root.val >= L && root.val <= R) {
            root.left = trimBST(root.left, L, R);
            root.right = trimBST(root.right, L, R);
            return root;

        } else if (root.val < L) {
            return  trimBST(root.right, L, R);
        } else // root.val > R
            return trimBST(root.left, L, R);
    }
}
