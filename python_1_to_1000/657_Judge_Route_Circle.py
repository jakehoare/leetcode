_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/judge-route-circle/
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle,
# which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are:
# R (Right), L (Left), U (Up) and D (down). The output should be true or false.

# Ensure that vertical and horizontal moves balance i.e. number of up and down moves are equal and number of left and
# right moves are equal.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")