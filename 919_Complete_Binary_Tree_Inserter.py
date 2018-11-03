_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/complete-binary-tree-inserter/
# A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
# and all nodes are as far left as possible.
# Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following:
# CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
# CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains
# complete, and returns the value of the parent of the inserted TreeNode;
# CBTInserter.get_root() will return the head node of the tree.

# Create a list of nodes of the tree from each row in order. Insert a new node by appending it to the list. Node's
# parent has index (i - 1) // 2 - 1 where i is node index (indices start from zero). Link parent to node according
# to parity of node index.
# Time - O(n) for init, O(1) for insert and get_root
# Space - O(n)

class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodelist = [root]

        for node in self.nodelist:          # list is extended by children during iteration
            if node.left:
                self.nodelist.append(node.left)
            if node.right:
                self.nodelist.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)                  # add new node to list
        self.nodelist.append(node)
        n = len(self.nodelist)

        parent = self.nodelist[(n // 2) - 1]
        if n % 2 == 0:
            parent.left = node
        else:
            parent.right = node

        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodelist[0]     # tree structure is maintained so just return root