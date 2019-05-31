_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
# Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original
# N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children.
# Similarly, a binary tree is a rooted tree in which each node has no more than 2 children.
# There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree
# can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.

# The left child of a binary node is the subtree encoding all the children of the corresponding n-ary node.
# The right child of a binary node is a chain of the binary root nodes encoding each sibling of the n-ary node.
# Hence the root node has no right binary child, because the root has no sibilings.
# Time - O(n)
# Space - O(n)

class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None

        binary = TreeNode(root.val)                 # create a binary root
        if not root.children:
            return binary

        binary.left = self.encode(root.children[0]) # left child of binary is the encoding of all n-ary children,
        node = binary.left                          #     starting with the first child.
        for child in root.children[1:]:             # other children of n-ary root are right child of previous child
            node.right = self.encode(child)
            node = node.right

        return binary

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None

        nary = Node(data.val, [])                   # create n-ary root
        node = data.left                            # move to first child of n-ary root
        while node:                                 # while more children of n-ary root
            nary.children.append(self.decode(node)) # append to list
            node = node.right                       # and move to next child

        return nary