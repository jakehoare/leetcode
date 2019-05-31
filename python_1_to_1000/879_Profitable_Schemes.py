_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/profitable-schemes/
# There are G people in a gang, and a list of various crimes they could commit.
# The i-th crime generates a profit[i] and requires group[i] gang members to participate.
# If a gang member participates in one crime, that member can't participate in another crime.
# Let's call a profitable scheme any subset of these crimes that generates at least P profit,
# and the total number of gang members participating in that subset of crimes is at most G.
# How many schemes can be chosen? Since the answer may be very large, return it modulo 10^9 + 7.

# Dynamic programming. For each job (with a profit and required gang), update a matrix of the number of schemes with
# each profit <= P and each gang <= G. Update the schemes for gang sizes at least as large as the job_gang, and for all
# profits where schemes with profits > P are included in the profits == P cells. Return all schemes with profit at
# least P for any gang size in the matrix.
# Time - O(NGP)
# Space - O(GP)

class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        schemes = [[0] * (G + 1) for _ in range(P + 1)]     # schemes[i][j] is nb schemes for profit i and gang j
        schemes[0][0] = 1

        for job_profit, job_gang in zip(profit, group):

            for p in range(P, -1, -1):                      # for schemes with all profits ...
                for g in range(G, job_gang - 1, -1):        # and enough members to do this job
                    capped_profit = min(P, p + job_profit)  # cap profit including this job at P
                    schemes[capped_profit][g] += schemes[p][g - job_gang]   # add schemes before this job

        return sum(schemes[-1]) % MOD                       # all schemes with profit at least P and gang <= G