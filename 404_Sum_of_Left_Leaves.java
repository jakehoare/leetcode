/*
https://leetcode.com/problems/sum-of-left-leaves/
Find the sum of all left leaves in a given binary tree.

Preorder travesal.  Base case return 0 for null.  Else if left node is a leaf add it to sum then add left and
right subtree left leaf sums.
Time - O(n)
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
    public int sumOfLeftLeaves(TreeNode root) {

        if (root == null)
            return 0;

        int leftLeafSum = 0;
        if (root.left != null && root.left.left == null && root.left.right == null)
            leftLeafSum += root.left.val;

        leftLeafSum += sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);

        return leftLeafSum;
    }
}