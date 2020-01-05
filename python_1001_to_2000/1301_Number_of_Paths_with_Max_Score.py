_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-paths-with-max-score/
# You are given a square board of characters.
# You can move on the board starting at the bottom right square marked with the character 'S'.
# You need to reach the top left square marked with the character 'E'.
# The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'.
# In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.
# Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect,
# and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
# In case there is no path, return [0, 0].

# Recursive helper function finds result from any cell.
# Base cases of outside board and "X" return no paths.
# Base case of "E" returns one path with maximum value zero.
# Recurse for the 3 possible moves. If all moves have no paths, return no paths.
# Else find the max value and sum all paths with that value.
# Memoize to avoid repetition.
# Time - O(mn)
# Space - O(mn)

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        rows, cols = len(board), len(board[0])
        visited = {}

        def helper(r, c):       # return [max_value, path_count] from board[r][c]
            if r < 0 or c < 0 or board[r][c] == "X":    # no paths
                return [0, 0]
            if (r, c) in visited:
                return visited[(r, c)]
            if r == 0 and c == 0:                       # "E" end cell
                return [0, 1]

            # 3 possible moves
            up_max, up_paths = helper(r - 1, c)
            left_max, left_paths = helper(r, c - 1)
            up_left_max, up_left_paths = helper(r - 1, c - 1)
            max_value, max_count_paths = 0, 0

            if up_paths + left_paths + up_left_paths > 0:   # no max_count_paths if no paths for any move
                max_value = max(up_max, left_max, up_left_max)
                if up_max == max_value:
                    max_count_paths += up_paths
                if left_max == max_value:
                    max_count_paths += left_paths
                if up_left_max == max_value:
                    max_count_paths += up_left_paths
                max_value += int(board[r][c]) if r < rows - 1 or c < cols - 1 else 0    # handle "S" start cell

            visited[(r, c)] = [max_value, max_count_paths]
            return [max_value, max_count_paths % MOD]

        return helper(rows - 1, cols - 1)
