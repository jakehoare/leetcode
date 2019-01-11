/*
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v
and w as descendants (where we allow a node to be a descendant of itself).

If p and q are on the same side as the root then recurse on that side.  Else if on different sides or
one of them is the root, return the root.  Assumes node.val are unique.
Time - O(n), worst case height of BST so log n if balanced
Space - O(1)
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if ((p.val - root.val) * (q.val - root.val) <= 0)
            return root;
        if (p.val > root.val)
            return lowestCommonAncestor(root.right, p, q);
        return lowestCommonAncestor(root.left, p, q);
    }
}
