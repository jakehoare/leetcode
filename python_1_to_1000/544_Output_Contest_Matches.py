_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/output-contest-matches/
# During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team, like make the
# rank 1 team play with the rank nth team, which is a good strategy to make the contest more interesting. Now, you're
# given n teams, you need to output their final contest matches in the form of a string.
# The n teams are given in the form of positive integers from 1 to n, which represents their initial rank. (Rank 1 is
# the strongest team and Rank n is the weakest team.) We'll use parentheses('(', ')') and commas(',') to represent the
# contest team pairing - parentheses('(' , ')') for pairing and commas(',') for partition. During the pairing process
# in each round, you always need to follow the strategy of making the rather strong one pair with the rather weak one.

# Create list of strings of all teams. While length of list > 1, iterate over list pairing first and last teams/matches
# (with brackets and comma to make new string) until middle.
# Time - O(n log n), final result is of length O(n log n) since each loop multiplies total string length by 2.5 times.
# Space - O(n)

class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = [str(i) for i in range(1, n + 1)]

        while len(result) > 1:
            new_result = []
            for i in range(len(result) // 2):
                new_result.append("(" + result[i] + "," + result[len(result) - i - 1] + ")")
            result = new_result

        return result[0]
