_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-genetic-mutation/
# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as
# ONE single character changed in the gene string.
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make
# it a valid gene string.
# Given start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from
# "start" to "end". If there is no such a mutation, return -1.
# Starting point is assumed to be valid, so it might not be included in the bank.
# You may assume start and end string is not the same.

# NOTE THAT THIS PROBLEM IS IN DRAFT STATUS IN LEETCODE
# BFS. For each gene in frontier, try all possible mutations. If mutation is in bank then remove, hence no need to
# check for loops.
# Time - O(n) where n is size of bank
# Space - O(n)

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        chars = set("ACGT")
        bank = set(bank)        # convert to a set
        if end not in bank:     # early return
            return -1
        distance = 0

        frontier = [start]
        while frontier:

            new_frontier = []
            distance += 1

            for gene in frontier:

                for i in range(len(gene)):
                    for c in chars:

                        if c == gene[i]:
                            continue

                        mutation = list(gene)           # convert to list, mutate and back to string
                        mutation[i] = c
                        mutation = "".join(mutation)

                        if mutation == end:             # ok since have returned early if end not in bank
                            return distance
                        if mutation in bank:
                            bank.discard(mutation)      # will not be shorter if same mutation is revisited
                            new_frontier.append(mutation)

            frontier = new_frontier

        return -1