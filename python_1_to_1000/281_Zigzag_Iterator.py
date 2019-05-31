_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/zigzag-iterator/
# Given two 1d vectors, implement an iterator to return their elements alternately.

# Maintain a queue of tuples (next vector, index in next vector) containing the next valid index and vector.  After
# iterating, add vector to back of queue if any more items remain.
# Time - O(k) (nb of vectors) to initialise vectors and q, O91) for next() and hasNext()
# Space - O(n), total number of items in all vectors

from collections import deque

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vectors = [v for v in (v1, v2) if v]                   # list of non-empty vectors
        self.q = deque((i, 0) for i in range(len(self.vectors)))    # queue of (index in vectors, index in vector)

    def next(self):
        """
        :rtype: int
        """
        vector, index = self.q.popleft()
        if index < len(self.vectors[vector])-1:
            self.q.append((vector, index+1))        # rejoin queue if not last item of vector
        return self.vectors[vector][index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)

