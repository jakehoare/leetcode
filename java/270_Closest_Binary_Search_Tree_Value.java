/*
https://leetcode.com/problems/closest-binary-search-tree-value/
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Update closest if current node is closer to target then previous closest.  Go left or right according to whether
target is above or below node.  Values in other subtree cannot be closes than current node.
Time - O(n), height of tree
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
    public int closestValue(TreeNode root, double target) {

        int closest = root.val;     // assumes root is not null

        while (root != null) {

            if (Math.abs(root.val - target) < Math.abs(closest - target))
                closest = root.val;

            root = target > root.val ? root = root.right : root.left;
        }

        return closest;
    }
}
