_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/distribute-candies/
# Given an integer array with even length, where different numbers in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to
# brother and sister. Return the maximum number of kinds of candies the sister could gain.

# Sisted get len(candies) // 2 candies. If there are this number or more of different candies, then sister can have
# all different candies. If there are fewer different kinds, then sister can have one of each kind.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) // 2, len(set(candies)))