_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-compressed-string-iterator/
# Design and implement a data structure for a compressed string iterator.
# It should support the following operations: next and hasNext.
# The given compressed string will be in the form of each letter followed by a positive integer representing the
# number of this letter existing in the original uncompressed string.
# next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.

# Serve the next letter on demand. Maintain the current letter and count of how many remaining unused instances.
# Also maintain index of next letter in compressedString.
# Time - O(n) for next, O(1) for init and hasNext.
# Space - O(1)

class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.letter = None
        self.count = 0              # number of current letter remaining
        self.i = 0                  # index of next letter after current is used
        self.s = compressedString

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return " "

        if self.count == 0:
            self.move()
        self.count -= 1             # decrement count of this letter
        return self.letter

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0 or self.i < len(self.s)

    def move(self):
        self.letter = self.s[self.i]
        self.count = 0
        self.i += 1

        while self.i < len(self.s) and self.s[self.i] <= "9":   # while digit
            self.count = self.count * 10 + int(self.s[self.i])  # update count with digit
            self.i += 1
