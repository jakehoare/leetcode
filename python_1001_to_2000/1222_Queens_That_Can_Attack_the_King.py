_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/queens-that-can-attack-the-king/
# On an 8x8 chessboard, there can be multiple Black Queens and one White King.
# Given an array of integer coordinates queens that represents the positions of the Black Queens,
# and a pair of coordinates king that represent the position of the White King,
# return the coordinates of all the queens (in any order) that can attack the King.

# For each of the 8 directions outwards from the king, move until a queen is reaches or the edge of the board.
# Time - O(1), since board is 8 x 8
# Space - O(1)

class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        queen_set = {tuple(queen) for queen in queens}

        result = []

        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            r, c = king
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r += dr
                c += dc
                if (r, c) in queen_set:
                    result.append([r, c])
                    break

        return result
