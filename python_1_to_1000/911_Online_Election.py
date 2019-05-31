_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/online-election/
# In an election, the i-th vote was cast for persons[i] at time times[i].
# Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number
# of the person that was leading the election at time t.
# Votes cast at time t will count towards our query.
# In the case of a tie, the most recent vote (among tied candidates) wins.

# Create a list of the leading candidate at each time. Add each candidate to a dictionary of counts. If there is a
# clear leader, update leader with thie candidate alone, else append candidate to leaders. Use max_count to identify
# whether a candidate is a leader.
# Binary search to look up a time. If time at index returned is later than t then return the leading candidate at
# the previous index. If time at index returned == t then return the leading candidate at that index.
# Time - O(n) for init, O(log n) for q
# Space - O(n)

from collections import defaultdict
import bisect

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.leader = []                        # leader[i] is the leading candidate at times[i]
        counts = defaultdict(int)               # cumulative count of votes for each candidate
        max_count = 0                           # number of votes for the leading candidate

        for person, time in zip(persons, times):

            counts[person] += 1

            if counts[person] > max_count:      # new unique leader
                max_count += 1
                leaders = [person]
            elif counts[person] == max_count:   # join other leaders
                leaders.append(person)

            self.leader.append(leaders[-1])     # most recent if tied

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        i = bisect.bisect_left(self.times, t)

        if i == len(self.times) or self.times[i] > t:
            return self.leader[i - 1]

        return self.leader[i]