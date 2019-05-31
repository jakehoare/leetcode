_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/can-place-flowers/
# Suppose you have a long flowerbed in which some of the plots are planted and some are not.
# However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
# and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

# Iterate over flowerbed. Check for flowers at i + 1, i and i - 1 in that order. If flower found, jump to next
# possible empty index. Else plant flower (decrement count, no need to amend flowerbed) and jump 2 indices.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.append(0)     # avoid special case for last index
        i = 0

        while n > 0 and i < len(flowerbed) - 1:

            if flowerbed[i + 1] == 1:
                i += 3
            elif flowerbed[i] == 1:
                i += 2
            elif i != 0 and flowerbed[i - 1] == 1:
                i += 1
            else:
                n -= 1
                i += 2

        return n == 0