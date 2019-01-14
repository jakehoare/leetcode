/*
https://leetcode.com/problems/construct-string-from-binary-tree/
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis
pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Add root node to string and return if no children. Add left subtree surrounded by brackets, hence empty brackets if
no subtree. Return without brackets if no right subtree, else add right subtree surrounded by brackets.
Time - O(n)
Space - O(1)
*/

class Solution {

    StringBuilder result = new StringBuilder();

    public String tree2str(TreeNode t) {
        helper(t);
        return result.toString();
    }

    private void helper(TreeNode node) {

        if (node == null)
            return;

        result.append(Integer.toString(node.val));

        if (node.left == null && node.right == null)
            return;
        result.append('(');
        helper(node.left);
        result.append(')');

        if (node.right == null)
            return;
        result.append('(');
        helper(node.right);
        result.append(')');
    }
}
