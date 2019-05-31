_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flower-planting-with-no-adjacent/
# You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.
# paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
# Also, there is no garden that has more than 3 paths coming into or leaving it.
# Your task is to choose a flower type for each garden such that, for any two gardens connected by a path,
# they have different types of flowers.
# Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.
# The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

# For each garden, plant a flower randomly chosen from the set of flowers that are not
# planted in any neighbouring garden.
# Time - O(n) since there are at most 3 paths for each garden.
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        edges = defaultdict(set)            # convert to map from garden to set of neighbouring gardens
        for i, j in paths:
            edges[i].add(j)
            edges[j].add(i)

        flowers = [None] * (N + 1)          # flowers[0] is not used

        for garden in range(1, N + 1):

            if flowers[garden]:
                continue
            possible_flowers = {1, 2, 3, 4} - {flowers[nbor] for nbor in edges[garden]}
            flowers[garden] = possible_flowers.pop()

        return flowers[1:]
