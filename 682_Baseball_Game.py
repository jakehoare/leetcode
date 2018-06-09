_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/baseball-game/
# You're now a baseball game point recorder.
# Given a list of strings, each string can be one of the 4 following types:
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score): The points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score): The points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation, which isn't a round's score): The last valid round's points were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
# You need to return the sum of the points you could get in all the rounds.

# Maintain a stack of previous scores, summed after applying all operations.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []

        for op in ops:

            if op == "+":               # assumes there are at least 2 previous socres
                points.append(points[-1] + points[-2])
            elif op == "D":             # assumes at least one previous score
                points.append(2 * points[-1])
            elif op == "C":             # remove previous
                points.pop()
            else:
                points.append(int(op))

        return sum(points)
