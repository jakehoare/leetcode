_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/dota2-senate/
# In the world of Dota2, there are two parties: the Radiant and the Dire.
# The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a
# change in the Dota2 game. The voting for this change is a round-based procedure.
# In each round, each senator can exercise one of the two rights:
# Ban one senator's right:  A senator can make another senator lose all his rights in this and all the following rounds.
# Announce the victory:  If this senator found the senators who still have rights to vote are all from the same party,
# he can announce the victory and make the decision about the change in the game.
# Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party
# and the Dire party respectively. Then if there are n senators, the size of the given string will be n.
# The round-based procedure starts from the first senator to the last senator in the given order. This procedure will
# last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
# Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which
# party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

# Create a queue of senator for each part by index. Compare the indices of the first senator from each party. The first
# will ban the rights of the second, so first is added to the back of the queue for this part and second is rejected.
# Time - O(n), total number of senators since one senator is removed in each step.
# Space - O(n)

from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        d, r = deque(), deque()         # indices of remaining senators for each party
        for i, c in enumerate(senate):
            if c == "D":
                d.append(i)
            else:
                r.append(i)

        while d and r:
            d_senator = d.popleft()
            r_senator = r.popleft()
            if d_senator < r_senator:
                d.append(d_senator + n)
            else:
                r.append(r_senator + n)

        return "Radiant" if r else "Dire"