_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/combination-sum-iii/
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can
# be used and each combination should be a unique set of numbers.

# Recursively add to partial solution all numbers greater than the previous number.
# Time - O(1), finite digits 1 to 9 implies fixed bound
# Space - O(1)

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        self.cs3([], n, results, k)
        return results

    def cs3(self, partial, target, results, k):

        if len(partial) == k and target == 0:   # result found
            results.append(partial)

        if len(partial) >= k or target <= 0:    # cannot make sum of n with k elements
            return

        last_used = 0 if not partial else partial[-1]
        for i in range(last_used+1, 10):        # add all greater digits than last_used
            self.cs3(partial + [i], target-i, results, k)
