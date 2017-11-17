/*
https://leetcode.com/problems/average-of-levels-in-binary-tree/
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Breadth-first search. Create a list of all non-null nodes at each level.
Time - O(n)
Space - O(n)
*/

class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> result = new ArrayList();

        if (root == null)
            return result;
        List<TreeNode> level = new ArrayList();     // list of nodes at current depth
        level.add(root);

        while (level.size() > 0) {

            long sum = 0;                           // avoid overflow
            List<TreeNode> newLevel = new ArrayList();

            for (TreeNode node : level) {
                sum += node.val;
                if (node.left != null)              // add non-null nodes
                    newLevel.add(node.left);
                if (node.right != null)
                    newLevel.add(node.right);
            }
            result.add((double) sum / (double) level.size());
            level = newLevel;
        }

        return result;
    }
}