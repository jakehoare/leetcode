_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-islands-ii/
# A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which
# turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of
# islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Union-find structure.  parent stores the parent island, self if not attached to any other land.  Number of
# unique neighbour islands are counted by ascending to ultimate parents, updating links to grandparents to compress
# paths and speed future lookups.  All connected neighbours are combined by union.
# Time - O(k log* k) where log* is iterated logarithm amd k is number of positions
# Space - O(k)

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        island_count = [0]
        parent = {}         # key is (r,c), value is parent (r,c)

        for r, c in positions:

            nbors = set()

            for nbor in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if nbor in parent:
                    island = parent[nbor]
                    while island != parent[island]:
                        parent[island] = parent[parent[island]]     # path compression
                        island = parent[island]
                    nbors.add(island)

            if not nbors:
                parent[(r, c)] = (r, c)             # own parent
                island_count.append(island_count[-1] + 1)
            else:
                this_island = nbors.pop()
                for nbor in nbors:
                    parent[nbor] = this_island
                parent[(r, c)] = this_island
                island_count.append(island_count[-1] - len(nbors))

        return island_count[1:]

