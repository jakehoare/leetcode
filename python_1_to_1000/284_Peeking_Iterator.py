_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/peeking-iterator/
# Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that
# supports the peek() operation -- i.e. returns the element that will be returned by the next call to next().

# Store the next iterator result and return it when peeking.
# Time - O(1)
# Space - O(1)

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.front = None
        self.it = iterator
        if self.it.hasNext():
            self.front = self.it.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.front   # None if not iterator.hasNext()

    def next(self):
        """
        :rtype: int
        """
        temp = self.front
        self.front = None
        if self.it.hasNext():   # replace front
            self.front = self.it.next()
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.front)
