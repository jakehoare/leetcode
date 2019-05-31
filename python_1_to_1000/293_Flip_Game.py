_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flip-game/
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters:
# + and -, you and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
# Write a function to compute all possible states of the string after one valid move.

# Iterate over s looking at pairs of chars and chaning any "++" to "--".
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []

        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                result.append(s[:i] + "--" + s[i + 2:])

        return result