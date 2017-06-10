/*
https://leetcode.com/problems/path-sum-iii/
You are given a binary tree in which each node contains an integer value. Find the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only
from parent nodes to child nodes).

Maintain a mapping from all sums on the current path to their counts. For each node, add to paths count if the
difference between partial sum to this node and some earlier path sum from mapping equals target. Increment current
partial sum in mapping and recurse left and right. Decrement partial sum count after recursing.
Time - O(n)
Space - O(n)
*/

public class Solution {
    Map<Integer, Integer> path_sums = new HashMap<Integer, Integer>();

    public int pathSum(TreeNode root, int sum) {
        path_sums.put(0, 1);            // default one count of zero sum
        return helper(root, 0, sum);
    }

    public int helper(TreeNode node, int partial, int target) {
        if (node == null)
            return 0;

        int paths = 0;
        partial += node.val;
        if (path_sums.containsKey(partial - target))
            paths += path_sums.get(partial - target);

        path_sums.put(partial, path_sums.getOrDefault(partial, 0) + 1);
        paths += helper(node.left, partial, target) + helper(node.right, partial, target);
        path_sums.put(partial, path_sums.get(partial) - 1);

        return paths;
    }
}