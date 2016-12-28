_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-the-celebrity/
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
# Now you want to find out who the celebrity is or verify that there is not one.
# The only thing you are allowed to do is to ask questions "Does A know B?".  You need to find out the celebrity (or
# verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# Find the only candidate by testing each person.  If the candidate knows that person, the candidate is not a celebrity
# and the new candidate is the test person.  If the candidate doesn't know that person, then that person is not a
# celebrity.  Note that there can be only one or zero celebrities.
# Then verify whether the candidate if valid.
# Time - O(n)
# Space - O(1)

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    return

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if i == candidate:
                continue
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        return candidate
