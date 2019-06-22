_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/letter-tile-possibilities/
# You have a set of tiles, where each tile has one letter tiles[i] printed on it.
# Return the number of possible non-empty sequences of letters you can make.

# Count the number of tiles of each type.
# Depth-first search for all possible sequences.
# Use each tile with a non-zero count and increment the number of sequences.
# Decrement the count of the used tile, then recurse. Increment the count back after recursion.
# Return when all tiles are used.
# Time - O(n!)
# Space - O(n!)

from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        self.total = 0
        freq = Counter(tiles)

        def helper(remaining):

            if remaining == 0:
                return

            for tile, count in freq.items():
                if count != 0:
                    freq[tile] -= 1
                    self.total += 1
                    helper(remaining - 1)
                    freq[tile] += 1

        helper(len(tiles))
        return self.total
