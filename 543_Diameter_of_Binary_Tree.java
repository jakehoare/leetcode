/*
https://leetcode.com/problems/diameter-of-binary-tree/
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

For each node, update max diameter as sum of depths of left and right subtrees.
Time - O(n)
Space - O(1)
*/

class Solution {
    int diameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return diameter;
    }

    private int depth(TreeNode node) {  // returns depth of deepest leaf, leaf node has depth of 1
        if (node == null)
            return 0;

        int left = depth(node.left);
        int right = depth(node.right);

        diameter = Math.max(diameter, left + right);
        return Math.max(left + 1, right + 1);
    }
}

