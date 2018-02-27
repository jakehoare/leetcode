/*
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree
has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among
its two sub-nodes.
Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value
in the whole tree. If no such second minimum value exists, output -1 instead.

Find the root value, which is the overall minimum. Then recurse through tree. Whenever we see a node with a value
greater than the root, update secondMinimum if necessary and stop since all node in that subtree are greater.
If we see a node with the same value as the root, explore its subtrees.
Time - O(n)
Space - O(n)
*/

class Solution {

    private int minimum;
    private int secondMinimum = Integer.MAX_VALUE;

    public int findSecondMinimumValue(TreeNode root) {

        if(root == null)
            return -1;
        minimum = root.val;

        searchTree(root);
        return secondMinimum == Integer.MAX_VALUE ? -1 : secondMinimum;
    }

    private void searchTree(TreeNode root) {

        if (root == null)
            return;

        if (root.val > minimum && root.val < secondMinimum) {
            secondMinimum = root.val;
            return;
        }

        searchTree(root.left);
        searchTree(root.right);
    }
}