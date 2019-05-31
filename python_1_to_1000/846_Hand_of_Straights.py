_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/hand-of-straights/
# Alice has a hand of cards, given as an array of integers.
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
# Return true if and only if she can.

# Sort the integers. Maintain a heap of partial straights. For each integer, if it's the same as the end of partial
# straight with the lowest end integer, start another partial straight. If it's more than 1 + the end of the first
# partial straight, this straight cannot be completed. Else extend the straight and complete it if length W.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:      # cannot make a whole number of straights
            return False
        if W == 1:
            return True

        hand.sort()
        partials = []               # heap of partial straights (last integer, straight length)

        for num in hand:

            if not partials or partials[0][0] == num:   # start a new straight
                heapq.heappush(partials, (num, 1))
                continue

            if num > partials[0][0] + 1:                # gap between num and end of first stright cannot be filled
                return False

            end, length = heapq.heappop(partials)       # num == partials[0][0] + 1, extend straight
            if length != W - 1:
                heapq.heappush(partials, (num, length + 1))

        return not partials
