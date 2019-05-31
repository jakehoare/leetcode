_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/rle-iterator/
# Write an iterator that iterates through a run-length encoded sequence.
# The iterator is initialized by RLEIterator(int[] A), where A is a run-length encoding of some sequence.
# More specifically, for all even i, A[i] tells us the number of times that the non-negative integer value A[i+1] is
# repeated in the sequence.
# The iterator supports one function: next(int n), which exhausts the next n elements (n >= 1) and returns the last
# element exhausted in this way.  If there is no element left to exhaust, next returns -1 instead.
# For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding of the sequence [8,8,8,5,5].
# This is because the sequence can be read as "three eights, zero nines, two fives".

# Maintain index of the count of the next element to be checked. While next requires mode elements than the current
# count, decrement the required n by the count and move to the next element. The decrement the count by n and return
# that element.
# Time - O(1) to initialize, O(n) for next
# Space - O(n)

class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.encoding = A
        self.length = len(A)
        self.i = 0                  # index of next count to be used

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.i < self.length and self.encoding[self.i] < n:   # require more elements than current count
            n -= self.encoding[self.i]      # use all elements
            self.i += 2                     # move to next count

        if self.i >= self.length:
            return -1

        self.encoding[self.i] -= n          # use some elements
        return self.encoding[self.i + 1]