/*
https://leetcode.com/problems/merge-two-binary-trees/
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are
overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up
as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Rescurside function. For base cases of either tree being null, return other tree (potentially also null). Else make
root from sum of nodes and rescurse left and right.
Time - O(n), total node in both trees
Space - O(n)
*/

class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {

        if (t1 == null)
            return t2;      // returns null if both t1 and t2 are null

        if (t2 == null)
            return t1;

        TreeNode root = new TreeNode(t1.val + t2.val);
        root.left = mergeTrees(t1.left, t2.left);
        root.right = mergeTrees(t1.right, t2.right);
        return root;
    }
}