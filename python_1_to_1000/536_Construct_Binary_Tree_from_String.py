_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/construct-binary-tree-from-string/
# You need to construct a binary tree from a string consisting of parenthesis and integers.
# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
# The integer represents the root value and a pair of parenthesis contains a child binary tree with the same structure.
# You always start to construct the left child node of the parent first if it exists.

# Instance variable i records next char to be processed. Convert root to TreeNode and increment i. If open bracket,
# skip and process left subtree. If another open bracket, skip and process right subtree. Skip closing bracket after
# either subtree.
# Time - O(n)
# Space - O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.i = 0          # index of next char of s to be processed

    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """

        def next_num():  # returns a TreeNode containing the integer at the prefix of s, also increments self.i
            num, neg = 0, False
            if s[self.i] == "-":
                neg = True
                self.i += 1
            while self.i < len(s) and s[self.i] not in {"(", ")"}:
                num = num * 10 + int(s[self.i])
                self.i += 1
            return TreeNode(-num) if neg else TreeNode(num)

        def helper():
            if self.i >= len(s):
                return None
            root = next_num()
            if self.i < len(s) and s[self.i] == "(":
                self.i += 1     # opening bracket
                root.left = helper()
                self.i += 1     # closing bracket
            if self.i < len(s) and s[self.i] == "(":
                self.i += 1     # opening bracket
                root.right = helper()
                self.i += 1     # closing bracket

            return root

        return helper()
