_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/combination-sum-ii/
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# Each number in C may only be used once in the combination.
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.

# Count the frequency of each number in candidates.  For each number subtract all possible numbers of copies up to
# the count and without exceeding target and recurse for the next number.  Alternative iterative version below.
# Time - O((f+1)^n) where f is the max frequency of any number and n is the number of distinct numbers

from collections import Counter

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        freq = list(Counter(candidates).items())
        self.combos(freq, 0, target, [], results)
        return results

    def combos(self, freq, next, target, partial, results):
        if target == 0:
            results.append(partial)
            return
        if next == len(freq):
            return

        for i in range(freq[next][1]+1):
            if i * freq[next][0] > target:
                break
            self.combos(freq, next+1, target-i*freq[next][0], partial + [freq[next][0]]*i, results)


# Iterative version of same procedure.
class Solution_Iterative(object):
    def combinationSum2(self, candidates, target):
        results = []
        partials = [[]]
        freq = list(Counter(candidates).items())

        for candidate, count in freq:

            new_partials = []
            for partial in partials:

                partial_sum = sum(partial)
                for i in range(count + 1):
                    if partial_sum + candidate*i < target:
                        new_partials.append(partial + [candidate]*i)
                    elif partial_sum + candidate*i == target:
                        results.append(partial + [candidate]*i)
                    if partial_sum + candidate*i >= target:
                        break

            partials = new_partials

        return results