_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/random-flip-matrix/
# You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are
# initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1,
# and then returns the position [row.id, col.id] of that value.
# Also, write a function reset which sets all values back to 0.
# Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

# Reduce 2D matrix to a 1D list of length rows * cols. For every random choice, increment the start index in the list
# and map the used number to an unused number that is now outside the [start, end] range. If random choice has been
# used already, get its mapping instead.
# If x has been chosen before use it
# Time - O(1)
# Space - O(k) number of calls to flip()

import random

class Solution(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.start, self.end = 0, n_rows * n_cols - 1
        self.used_to_free = {}      # map chosen random ints to an unchosen ints outside [start, end]
        self.cols = n_cols

    def flip(self):
        """
        :rtype: List[int]
        """
        x = random.randint(self.start, self.end)
        index = self.used_to_free.get(x, x)         # returned index is x if not used, else mapping of x
        self.used_to_free[x] = self.used_to_free.get(self.start, self.start) # map x to start or mapping of start
        self.start += 1
        return list(divmod(index, self.cols))       # convert index to 2d coordinates

    def reset(self):
        """
        :rtype: void
        """
        self.start = 0
        self.used_to_free = {}