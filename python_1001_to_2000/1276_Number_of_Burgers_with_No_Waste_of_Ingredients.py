_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:
# Jumbo Burger: 4 tomato slices and 1 cheese slice.
# Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0
# and the number of remaining cheeseSlices equal to 0.
# If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

# We cannot reach a solution for an odd number of tomato or tomato less than 2 * cheese or tomato more than 4 * cheese.
# Else solve the linear equations:
#   jumbo + small = cheese
#   4 * jumbo + 2 * small = tomato
# Time - O(1)
# Space - O(1)

class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if tomatoSlices % 2 == 1 or tomatoSlices < 2 * cheeseSlices or tomatoSlices > 4 * cheeseSlices:
            return []

        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo
        return [jumbo, small]
