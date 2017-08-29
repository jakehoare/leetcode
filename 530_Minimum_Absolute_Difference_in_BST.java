/*
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any
two nodes.

Inorder traversal. Update minDiff if not first node. Update previous.
Time - O(n)
Space - O(i)
*/

class Solution {
    private int previous;
    private int minDiff = -1;   // -1 no nodes visited yet

    private void inOrder(TreeNode node) {
        if (node == null)
            return;

        inOrder(node.left);

        if (minDiff != -1)      // not first node, update max
            minDiff = Math.min(minDiff, Math.abs(node.val - previous));
        else                    // first node
            minDiff = Integer.MAX_VALUE;
        previous = node.val;

        inOrder(node.right);
    }

    public int getMinimumDifference(TreeNode root) {
        inOrder(root);
        return minDiff;
    }
}
