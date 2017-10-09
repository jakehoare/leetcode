/*
https://leetcode.com/problems/subtree-of-another-tree/
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a
subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Serialise each tree with special symbol for null. Preceed each node with ",".
Time - O(m*n) because contains() performs naive pattern matching. KMP is O(m + n)
Space - O(m + n)
*/

class Solution {
    StringBuilder sb = new StringBuilder();
    public boolean isSubtree(TreeNode s, TreeNode t) {

        serialize(s);
        String sSerial = sb.toString();
        sb.setLength(0);
        serialize(t);
        String tSerial = sb.toString();

        return sSerial.contains(tSerial);
    }

    private void serialize(TreeNode node) {

        sb.append(",");     // preceed each node with "," to encode s = [1]
                            // as ",1,#,#" and so not be a subtree of t = [21]

        if (node == null) {
            sb.append("#"); // assume "#" cannot be a node.val
            return;
        }

        sb.append(Integer.toString(node.val));
        serialize(node.left);
        serialize(node.right);
    }
}