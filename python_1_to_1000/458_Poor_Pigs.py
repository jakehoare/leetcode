_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/poor-pigs/
# There are 1000 buckets, one and only one of them contains poison, the rest are filled with water.
# They all look the same. If a pig drinks that poison it will die within 15 minutes.
# What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
# Answer this question, and write an algorithm for the follow-up general case.
# If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out
# the "poison" bucket within p minutes? There is exact one bucket with poison.

# Find the number of rounds of tests that can be run as the integer division of the total time over time to die.
# Arrange the buckets in a hypercube with side of rounds + 1.
# Each pig finds the coordinate in one dimension of the hypercube by drinking from rounds + 1 buckets in each round.
# If a pig dies, we find the coordinate in that dimension, if it doesn't we know the coordinate is the final index.
# Hence buckets in hypercube = (rounds + 1) ** pigs. So pigs = ln(buckets) / ln(rounds + 1), rounded up to the next
# integer.
# Time - O(1)
# Space - O(1)

from math import log, ceil

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        rounds = minutesToTest // minutesToDie

        return int(ceil(log(buckets) / log(rounds + 1)))