_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/nested-list-weight-sum-ii/
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from
# bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

# DFS to calculate the sum of integers at each depth, starting with the shallowest.  When max_depth is known,
# weight each depth sum by its number of layers above max_depth.
# Alternatively, BFS calculating the cumulative unweighted sum and repeatedly adding it at each depth.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth_sums = []             # depth_sums[i] is the sum of integers at depth i
        for nested in nestedList:
            self.dfs(nested, 0, depth_sums)

        total = 0
        max_depth = len(depth_sums)
        for i, depth_sum in enumerate(depth_sums):
            total += (max_depth - i) * depth_sum
        return total


    def dfs(self, nested, depth, depth_sums):
        if len(depth_sums) <= depth:    # new depth, extend list
            depth_sums.append(0)

        if nested.isInteger():          # add to sum at depth
            depth_sums[depth] += nested.getInteger()
        else:
            for n in nested.getList():  # recurse at greater depth
                self.dfs(n, depth + 1, depth_sums)

class Solution2(object):
    def depthSumInverse(self, nestedList):
        unweighted, weighted = 0, 0
        q = nestedList

        while q:
            new_q = []

            for nested in q:
                if nested.isInteger():
                    unweighted += nested.getInteger()
                else:
                    new_q += nested.getList()

            q = new_q
            weighted += unweighted

        return weighted
