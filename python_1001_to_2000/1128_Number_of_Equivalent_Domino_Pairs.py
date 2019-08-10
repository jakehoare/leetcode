_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if
# either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length,
# and dominoes[i] is equivalent to dominoes[j].

# Dictionary counts previously seen dominoes.
# Iterate over dominoes, rotating each so the greatest number is first.
# Convert to tuple so they can be added to dictionary.
# Add to the result all pairs formed with equivalent dominoes.
# Time - O(n)
# Space - O(1)

from collections import defaultdict

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        seen = defaultdict(int)             # map canonical dominoe to its count
        result = 0

        for domino in dominoes:
            if domino[0] > domino[1]:       # put greatest first
                domino = domino[::-1]

            domino_tuple = tuple(domino)
            result += seen[domino_tuple]    # add pairs with all equivalent
            seen[domino_tuple] += 1

        return result
