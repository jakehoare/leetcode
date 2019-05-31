_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/possible-bipartition/
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
# Each person may dislike some other people, and they should not go into the same group.
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
# Return true if and only if it is possible to split everyone into two groups in this way.

# Map each person to the set of people they dislike. For each person, put them in a group then find all the people
# they dislike. If any of the disliked are in the group then return False, else remove from disliked all those already
# in the other group, swap the groups and repeat by placing the disliked.
# Time - O(n**2), the length of dislikes
# Space - O(n**2)

from collections import defaultdict

class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        dislike = defaultdict(set)          # map each person to the set of people they dislike
        for a, b in dislikes:
            dislike[a].add(b)
            dislike[b].add(a)

        this, other = set(), set()          # 2 groups of people

        for i in range(1, N + 1):

            if i in this or i in other:     # already placed this person in a group
                continue
            to_add = {i}

            while to_add:

                this |= to_add              # put to_add in this

                disliked = set()            # people disliked by the people in to_add
                for num in to_add:
                    disliked |= dislike[num]
                if disliked & this:         # somebody dislikes somebody else in this group
                    return False

                disliked -= other           # remove people already in other
                to_add = disliked
                this, other = other, this

        return True