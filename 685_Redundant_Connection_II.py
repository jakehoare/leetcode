_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/redundant-connection-ii/
# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all
# other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which
# has no parents.
# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N),
# with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not
# an edge that already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a
# directed edge connecting nodes u and v, where u is a parent of child v.
# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.
# If there are multiple answers, return the answer that occurs last in the given 2D-array.

# Given a valid tree, a redundant connection is either A) to the root, causing all nodes to have one parent or B) not
# to the root, causing some node to have 2 parents. If case B, find the node with 2 parents and the root. Remove one
# of the incoming edges to the node with 2 parents and if the tree is valid, the removed edge is redundant else the
# other incoming edge to the node with 2 parents is redundant.
# If case A, try removing edges from the last of the input list until a valid tree is found.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parents = [[] for _ in range(n + 1)]
        nbors = [set() for _ in range(n + 1)]

        for a, b in edges:                      # build parents and nbors lists
            parents[b].append(a)
            nbors[a].add(b)

        root = None
        for i, parent in enumerate(parents):    # check if some node has 2 parents
            if len(parent) == 2:
                two_parents = i
            if not parent:                      # identify the root
                root = i

        def valid(root):                        # test if all nodes can be visited once and once only
            visited = set()
            queue = [root]
            while queue:
                node = queue.pop()
                if node in visited:
                    return False
                visited.add(node)
                queue += nbors[node]
            return len(visited) == n

        if root:                                # case B, edge added to node that was not root
            p1, p2 = parents[two_parents]
            nbors[p2].discard(two_parents)      # discard second edge
            return [p2, two_parents] if valid(root) else [p1, two_parents]

        for i in range(len(edges) - 1, -1, -1): # remove edges starting with last edge to be added
            n1, n2 = edges[i]
            nbors[n1].discard(n2)               # temporarily remove edge from n1 to n2
            if valid(n2):                       # n2 becomes the root
                return edges[i]
            nbors[n1].add(n2)                   # put edge back