_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
# In a social group, there are N people, with unique integer ids from 0 to N-1.
# We have a list of logs, where each logs[i] = [timestamp, id_A, id_B] contains a non-negative integer timestamp,
# and the ids of two different people.
# Each log represents the time in which two different people became friends.
# Friendship is symmetric: if A is friends with B, then B is friends with A.
# Let's say that person A is acquainted with person B if A is friends with B,
# or A is a friend of someone acquainted with B.
# Return the earliest time for which every person became acquainted with every other person.
# Return -1 if there is no such earliest time.

# Sort by time. Union-find groups of friends.
# Intially each person is in their own group.
# For each pair of new friends, find their group leaders and if not the same leader then join the groups.
# Keep count of the number of groups.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs.sort()                         # sort by ascending time
        friend = {i: i for i in range(N)}   # map person to a friend
        groups = N

        def leader(i):                      # find exemplar amongst a group of friends
            while friend[i] != i:
                i = friend[i]
            return i

        for time, A, B in logs:
            a, b = leader(A), leader(B)
            if a != b:
                friend[a] = b               # join the groups and decrement the group count
                groups -= 1
                if groups == 1:             # everybody is friends
                    return time

        return -1
