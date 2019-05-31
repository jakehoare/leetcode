_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node
# has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work.
# Ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the tree structure.

# Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed, so the
# function returns to its parent call.
# Deserialize by creating a deque (could also use an iterator with next() instead of popleft()). While the next item is
# not "#", create a child with the item, add the child to the list of children and recurse to create its subtree.
# Repeat until there are no more children, then ignore the "#".
# Time - O(n)
# Space - O(n)

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: Node
        :rtype: str
        """
        serial = []

        def preorder(node):

            if not node:
                return

            serial.append(str(node.val))

            for child in node.children:
                preorder(child)

            serial.append("#")      # indicates no more children, continue serialization from parent

        preorder(root)
        return " ".join(serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def helper(node):

            if not tokens:
                return

            while tokens[0] != "#": # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()        # discard the "#"

        helper(root)
        return root