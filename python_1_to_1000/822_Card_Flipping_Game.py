_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/card-flipping-game/
# On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).
# We flip any number of cards, and after we choose one card.
# If the number X on the back of the chosen card is not on the front of any card, then this number X is good.
# What is the smallest number that is good?  If no number is good, output 0.
# Here, fronts[i] and backs[i] represent the number on the front and back of card i.
# A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

# Iterate over both lists, finding cards with duplicate number of front and back.
# Then iterate again, if a pair of numbers are different then each number that is not a duplicate can potentially
# be a solution.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        duplicates = {f for f, b in zip(fronts, backs) if f == b}
        result = float("inf")

        for f, b in zip(fronts, backs):
            if f != b:
                if f not in duplicates:
                    result = min(result, f)
                if b not in duplicates:
                    result = min(result, b)

        return 0 if result == float("inf") else result