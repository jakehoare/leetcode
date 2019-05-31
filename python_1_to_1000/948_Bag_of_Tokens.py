_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bag-of-tokens/
# You have an initial power P, an initial score of 0 points, and a bag of tokens.
# Each token can be used at most once, has a value token[i], and has potentially two ways to use it.
# If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
# If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
# Return the largest number of points we can have after playing any number of tokens.

# Sort the tokens. Use as many low value tokens to get as many points as possible. Then repeatedly use the highest
# value token to convert one point into power and use as many low value tokens to convert all available
# power into points.
# Time - O(n)
# Space - O(1)

class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        points, power = 0, P
        left, right = 0, len(tokens) - 1

        tokens.sort()

        while left < len(tokens) and tokens[left] <= power:
            power -= tokens[left]
            points += 1
            left += 1

        if not points:      # never possible to have any points
            return 0

        while right - left > 1:

            points -= 1
            power += tokens[right]
            right -= 1

            while right - left >= 0 and tokens[left] <= power:
                power -= tokens[left]
                points += 1
                left += 1

        return points