_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/satisfiability-of-equality-equations/
# Given an array equations of strings that represent relationships between variables, each string equations[i] has
# length 4 and takes one of two different forms: "a==b" or "a!=b".
# Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.
# Return true if and only if it is possible to assign integers to variable names to satisfy all the given equations.

# Create an undirected graph mapping each variable to the list of variables it is equal to.
# Mark all connected variables as belonging to the same group.
# Return false if any pair of not equal variables belong to the same group.
# Alternatively, union-find.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        graph = [[] for _ in range(26)]         # map of variable to equal variables
        not_equal = []                          # tuples of not equal variables

        for eqn in equations:
            first, op, second = eqn[0], eqn[1], eqn[3]
            first, second = ord(first) - ord("a"), ord(second) - ord("a")   # convert letter variables to integers

            if op == "=":
                graph[first].append(second)
                graph[second].append(first)
            else:
                not_equal.append((first, second))

        groups = [None] * 26                    # group index of equal variables

        def dfs(node, group):
            if groups[node] is None:
                groups[node] = group
                for nbor in graph[node]:
                    dfs(nbor, group)

        for i in range(26):                     # if not already set, set connected variable group index
            dfs(i, i)

        for first, second in not_equal:
            if groups[first] == groups[second]:
                return False

        return True
