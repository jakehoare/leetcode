/*
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their
sum is equal to the given target.

Sets stores seen values. Fro each node, check if complimnet has been seen, if not add to set and recurse on thildren.
The fact that it is a BST rather than a binary tree is irrelevant.
Time - O(n)
Space - O(n)
*/

class Solution {

    public boolean findTarget(TreeNode root, int k) {

        Set seen = new HashSet<Integer>();
        return helper(root, k, seen);
    }

    private boolean helper(TreeNode node, int k, Set seen) {

            if (node == null)
                return false;
            if (seen.contains(k - node.val))
                return true;

            seen.add(node.val);
            return (helper(node.left, k, seen) || helper(node.right, k, seen));
    }

}