_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/random-pick-with-blacklist/
# Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer
# from [0, N) which is NOT in B.
# Optimize it such that it minimizes the call to system’s Math.random().

# Create a mapping so that all of the allowed numbers are together. Make the first part of the array the allowed
# whitelist. Find a list of all white numbers that are not in the first part of the array. For each black number that
# is in the first part of the array, map it to a white number that is not in the first part.
# Pick random indices from the length of the whitelist. If a number is mapped from black to white, return its mapping
# else the number is not blacklisted so return it.
# Time - O(n) for init, O(1) for pick.
# Space - O(n)

from random import randint

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.white = N - len(blacklist)         # number of non-black numbers
        blacklist = set(blacklist)
        self.white_to_move = [i for i in range(self.white, N) if i not in blacklist]
        self.mapping = {b : self.white_to_move.pop() for b in blacklist if b < self.white}

    def pick(self):
        """
        :rtype: int
        """
        rand = randint(0, self.white - 1)
        return self.mapping[rand] if rand in self.mapping else rand