_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/
# Given a rectangle of size n x m, find the minimum number of integer-sided squares that tile the rectangle.

# State consists of the height of each column already tiled.
# Given a state, find the lowest column and its index.
# For each adjacent column with the height of the lowest column, add a square and recurse.
# Time - O(m**3 n), mn possible states each taking O(m ** 2) to construct
# Space - O(m**2 n)

class Solution(object):
    def tilingRectangle(self, rows, cols):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if cols > rows:  # swap so cols <= rows
            cols, rows = rows, cols

        memo = {}

        def dp(state):
            if min(state) == rows:  # each col has height of rows
                return 0
            if state in memo:
                return memo[state]

            min_height = min(state)
            start = state.index(min_height)
            result = cols * rows

            state_list = list(state)
            for end in range(start, cols):
                if state[end] != min_height:
                    break
                side = end - start + 1
                if min_height + side > rows:    # insufficient height
                    break
                state_list[start: end + 1] = [min_height + side] * side
                result = min(result, dp(tuple(state_list)))

            memo[state] = result + 1
            return result + 1

        return dp(tuple([0] * cols))