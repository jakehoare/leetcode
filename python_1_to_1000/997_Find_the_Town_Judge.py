_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-the-town-judge/
# In a town, there are N people labelled from 1 to N.
# There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that person labelled a trusts person labelled b.
# If the town judge exists and can be identified, return the label of the town judge. Otherwise, return -1.

# Count the net balance of the number of people trusting each person. If person A trusts person B, increment the count
# of B and decrement the count of A. The judge must be trusted by everybody and trust nobody, so has a count of N - 1.
# Time - O(n**2) for n people
# Space - O(n)

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_count = [0] * (N + 1)

        for trustee, trusted in trust:
            trust_count[trusted] += 1
            trust_count[trustee] -= 1

        for person in range(1, N + 1):
            if trust_count[person] == N - 1:
                return person

        return -1
