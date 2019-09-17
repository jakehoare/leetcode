_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-distance-to-target-color/
# You are given an array colors, in which there are three colors: 1, 2 and 3.
# You are also given some queries.
# Each query consists of two integers i and c,
# return the shortest distance between the given index i and the target color c.
# If there is no solution return -1.

# For each element of the array, find the distance to the closest element of each color to the left.
# Then update the closest distance to each color for each index, with any closer indices on the right.
# For each query index, lookup the closest distance to the required color.
# Time - O(m + n) for array of length m and n queries.
# Space - O(m + n)

class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        shortest = []
        distances = [float("inf")] * 3                  # to next element of each color on left
        for color in colors:
            distances = [d + 1 for d in distances]      # add 1 to distance for each color
            distances[color - 1] = 0                    # zero distance to thie color
            shortest.append(list(distances))

        for i in range(len(colors) - 2, -1, -1):        # update with closest color on right, if smaller
            distances = [d + 1 for d in shortest[i + 1]]
            for color in range(3):
                shortest[i][color] = min(shortest[i][color], distances[color])

        result = []
        for i, color in queries:
            shortest_dist = shortest[i][color - 1]
            result.append(-1 if shortest_dist == float("inf") else shortest_dist)

        return result
