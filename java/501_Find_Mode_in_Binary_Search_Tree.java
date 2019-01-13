/*
https://leetcode.com/problems/find-mode-in-binary-search-tree/
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the
given BST. Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Inorder traversal visits nodes in increasing order. Find length of longest sequence of same val. Repeat inorder
traversal finding all vals with maxFreq.
Time - O(n)
Space - O(1), alternatively Morris traversal avoids recursion
*/

class Solution {

    private int current = 0;
    private int freq = 0;
    private int maxFreq = 0;
    private List<Integer> modes = new ArrayList<Integer>();

    private void findGreatestFrequency(TreeNode node) {

        if (node == null)
            return;

        findGreatestFrequency(node.left);

        if (current != node.val) {
            current = node.val;
            freq = 0;
        }
        ++freq;
        maxFreq = Math.max(maxFreq, freq);

        findGreatestFrequency(node.right);
    }

    private void findModes(TreeNode node) {

        if (node == null)
            return;

        findModes(node.left);

        if (current != node.val) {
            current = node.val;
            freq = 0;
        }
        ++freq;
        if (freq == maxFreq)
            modes.add(current);

        findModes(node.right);
    }

    public int[] findMode(TreeNode root) {
        findGreatestFrequency(root);
        freq = 0;
        findModes(root);

        int[] result = new int[modes.size()];
        for (int i = 0; i < modes.size(); ++i)
            result[i] = modes.get(i);
        return result;
    }
}
