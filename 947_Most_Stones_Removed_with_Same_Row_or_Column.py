_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
# What is the largest possible number of moves we can make?

# Any connected component of the graph (points are connected by a common row or column) can be reduced to a single
# point by repeatedly pruning.
# Use union-find tree to identify rows and columns that are connected. Remove all stones apart from one per
# connected component.
# Time - O(n log n)
# Space - O(n)

class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parents = {}                    # map row or column to its parent

        def find(x):
            while x != parents[x]:
                x = parents[x]
            return x

        def union(x, y):
            parents.setdefault(x, x)    # sets parents[x] to x if not in dictionary
            parents.setdefault(y, y)
            parents[find(x)] = find(y)

        for i, j in stones:
            union(i, ~j)                # ~j == -j - 1, so columns are distinct from rows

        return len(stones) - len({find(x) for x in parents})