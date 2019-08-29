_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/analyze-user-website-visit-pattern/
# We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].
# A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
# The websites in a 3-sequence are not necessarily distinct.
# Find the 3-sequence visited by the largest number of users. If there is more than one solution,
# return the lexicographically smallest such 3-sequence.

# Make a time-ordered list of sites for each user.
# For each list, find all patterns of 3 ordered sites.
# Map each pattern to all users with that pattern.
# Find the pattern with the most users.
# Time - O(n**3) for n visits.
# Space - O(n**3)

from collections import defaultdict

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        user_sites = defaultdict(list)          # user mapped to list of sites in time order.
        for _, user, site in sorted(zip(timestamp, username, website)):
            user_sites[user].append(site)

        pattern_to_count = defaultdict(set)     # map 3-sequence to users with that 3-sequence
        for user, sites in user_sites.items():
            n = len(sites)
            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        pattern_to_count[(sites[i], sites[j], sites[k])].add(user)

        max_count = len(max(pattern_to_count.values(), key=len))    # count of mos popular 3-sequence
        return min(key for key, value in pattern_to_count.items() if len(value) == max_count)
