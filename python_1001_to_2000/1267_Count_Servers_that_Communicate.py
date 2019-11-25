_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-servers-that-communicate/
# You are given a map of a server center, represented as a m * n integer matrix grid,
# where 1 means that on that cell there is a server and 0 means that it is no server.
# Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

# Iterate over grid, counting the number of servers in each row and each column.
# The iterate over grid again, incrementing the result for each server that has another server on the same
# row or column.
# Alternatively, store all servers in first loop to avoid iterateing over entire grid twice but use more space.
# Time - O(mn)
# Space - O(m + n)

class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        row_servers, cols_servers = [0] * rows, [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_servers[r] += 1
                    cols_servers[c] += 1

        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_servers[r] > 1 or cols_servers[c] > 1):
                    result += 1

        return result

class Solution2(object):
    def countServers(self, grid):
        rows, cols = len(grid), len(grid[0])
        row_servers, cols_servers = [0] * rows, [0] * cols
        servers = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_servers[r] += 1
                    cols_servers[c] += 1
                    servers.add((r, c))

        return sum(1 for r, c in servers if row_servers[r] > 1 or cols_servers[c] > 1)