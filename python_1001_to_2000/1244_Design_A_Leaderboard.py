_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-a-leaderboard/
# Design a Leaderboard class, which has 3 functions:
# addScore(playerId, score): Update the leaderboard by adding score to the given player's score.
# If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
# top(K): Return the score sum of the top K players.
# reset(playerId): Reset the score of the player with the given id to 0.
# It is guaranteed that the player was added to the leaderboard before calling this function.
# Initially, the leaderboard is empty.

# Map the user to a score.
# Make a heap of the K largest values for top.
# Time - O(1) for addScore and reset, O(n log n) for top
# Space - O(n)

from collections import defaultdict
import heapq

class Leaderboard(object):

    def __init__(self):
        self.user_score = defaultdict(int)

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        self.user_score[playerId] += score

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        return sum(heapq.nlargest(K, self.user_score.values()))

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.user_score[playerId]
