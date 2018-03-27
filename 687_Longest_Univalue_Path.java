/*
https://leetcode.com/problems/longest-univalue-path/
Given a binary tree, find the length of the longest path where each node in the path has the same value.
This path may or may not pass through the root.
The length of path between two nodes is represented by the number of edges between them.

Helper function return an array with the max paths via left and right children of a node. If a node has a child and
the child has the same val then it has max path via that child of 1 + max(left and right child paths).
Time - O(n)
Space - O(n)
*/

class Solution {

    int longest = 0;

    public int longestUnivaluePath(TreeNode root) {
        helper(root);
        return longest;
    }

    private int[] helper(TreeNode node) {

        int[] paths = {0, 0};
        if (node == null)
            return paths;

        int[] leftPath = helper(node.left);
        int[] rightPath = helper(node.right);
        if (node.left != null && node.left.val == node.val)
            paths[0] = 1 + Math.max(leftPath[0], leftPath[1]);
        if (node.right != null && node.right.val == node.val)
            paths[1] = 1 + Math.max(rightPath[0], rightPath[1]);

        longest = Math.max(longest, paths[0] + paths[1]);
        return paths;
    }
}