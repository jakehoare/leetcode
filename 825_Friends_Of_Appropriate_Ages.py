_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/friends-of-appropriate-ages/
# Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.
# Person A will NOT friend request person B (B != A) if any of the following conditions are true:
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.
# Note that if A requests B, B does not necessarily request A. Also, people will not friend request themselves.
# How many total friend requests are made?

# Group all people of same age together and sort by age. For each age, only consider younger people. Add to result
# all pairs where b > 0.5 * a + 7 and (b < 100 or a > 100). Add all pairs of the same age if over 14 (age > 0.5 age + 7)
# Time - O(n**2)
# Space - O(n)

from collections import Counter

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        freq = Counter(ages)
        age_counts = [(k, v) for k, v in freq.items()]
        age_counts.sort()
        requests = 0

        for a, (age_a, count_a) in enumerate(age_counts):

            for age_b, count_b in age_counts[:a]:       # age_b < age_a
                if age_b > 0.5 * age_a + 7 and (age_b < 100 or age_a > 100):
                    requests += count_a * count_b

            if age_a > 14:                              # people of same age
                requests += count_a * (count_a - 1)

        return requests