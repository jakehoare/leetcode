_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/evaluate-division/
# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real
# number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

# Create a graph with nodes as variables and directed edge A->B weighted by the ratio A/B. Floyd-Warshall calculates
# weights of paths between all pairs of nodes by iteratively adding paths between 2 nodes (j and k) that can be reached
# from node i.
# Time - O(n**3) where n is number of variables
# Space - O(n**2)

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)           # outer dict key is source node, value is destination node
        for i in range(len(equations)):     # innder dict key is destination node, value is ratio
            num, den, val = equations[i][0], equations[i][1], values[i]
            graph[num][den] = val
            graph[den][num] = 1 / val

        for i in graph:
            for j in graph[i]:
                for k in graph[i]:
                    graph[j][k] = graph[j][i] * graph[i][k]     # graph[j][j] = 1

        results = []
        for num, den in queries:
            if num in graph and den in graph[num]:
                results.append(graph[num][den])
            else:
                results.append(-1)
        return results


