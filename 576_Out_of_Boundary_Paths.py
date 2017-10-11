_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/out-of-boundary-paths/
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent
# cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times.
# Find out the number of paths to move the ball out of grid boundary. The answer may be very large,
# return it after mod 10^9 + 7.

# Dynamic programming. For each time step, calculate the nb paths to reach each cell. Running total of paths to reach
# boundary is increased at each step by number of previous paths to cells next to edge. Update paths at next step
# according to sum of all paths to neighbour cell from previous step.
# Alternatively, recursion requires more space but is practically faster.
# Time - O(m * n * N)
# Space - O(m * n)

class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        paths = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]  # nb paths to reach each cell
        dp[i][j] = 1  # intially 1 for start position

        for _ in range(N):

            new_dp = [[0 for _ in range(n)] for _ in range(m)]

            for r in range(m):
                for c in range(n):

                    if r == 0:
                        paths += dp[r][c]
                    if r == m - 1:
                        paths += dp[r][c]
                    if c == 0:
                        paths += dp[r][c]
                    if c == n - 1:
                        paths += dp[r][c]
                    paths %= 10 ** 9 + 7

                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if 0 <= r + dr < m and 0 <= c + dc < n:
                            new_dp[r + dr][c + dc] += dp[r][c]
                    new_dp[r][c] %= 10 ** 9 + 7

            dp = new_dp

        return paths



class Solution2(object):
    def findPaths(self, m, n, N, i, j):

        def helper(r, c, steps):

            if steps == 0:
                return 0

            if (r, c, steps) in memo:
                return memo[(r, c, steps)]

            paths = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    paths += helper(r + dr, c + dc, steps - 1)
                else:
                    paths += 1  # one path to exit grid
                paths %= 10 ** 9 + 7

            memo[(r, c, steps)] = paths
            return paths

        memo = {}
        return helper(i, j, N)


