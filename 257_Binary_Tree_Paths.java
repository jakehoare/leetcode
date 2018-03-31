/*
https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.

Top-down recursively add node.val to path and recurse if node is not a leaf, or store result for leaves.
Alternatively, bottom-up find all paths from left and right nodes to leaves a prepend current node.
Both can be converted to use StringBuilder but leaf node values must be removed from path after toString() in order
to revert to original path.
Time - O(n**2), for every node visited extend existing path
Space - O(n)
*/

public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<String>();       // LinkedList also works
        helper(root, "", paths);
        return paths;
    }

    public void helper(TreeNode node, String path, List<String> paths) {
        if (node == null)
            return;
        if (node.left == null && node.right == null)        // leaf node, add to result
            paths.add(path + node.val);
        helper(node.left, path + node.val + "->", paths);
        helper(node.right, path + node.val + "->", paths);
    }
}


public class Solution2 {
    public List<String> binaryTreePaths(TreeNode root) {

        List<String> paths = new ArrayList<String>();

        if (root == null)
            return paths;

        if (root.left == null && root.right == null) {
            paths.add(Integer.toString(root.val));
            return paths;
        }

        List<String> left_paths = binaryTreePaths(root.left);
        List<String> right_paths = binaryTreePaths(root.right);

        for (String p : left_paths)
            paths.add(root.val + "->" + p);
        for (String p : right_paths)
            paths.add(root.val + "->" + p);

        return paths;
    }
}