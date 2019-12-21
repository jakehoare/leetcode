_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/iterator-for-combination/
# Design an Iterator class, which has:
# A constructor that takes a string characters of sorted distinct lowercase English letters
# and a number combinationLength as arguments.
# A function next() that returns the next combination of length combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next combination.

# Maintain a combination, which is a list of indices of characters of the next combination.
# Also set the final combination as combinationLength indices ending with the last index of characters.
# Find the next combination by iterating backwards to find an index that is less than its final index.
# Increment the index and set all later indices in ascending order.
# Time - O(1) for init and hasNext, O(n) for next
# Space - O(n)

class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.chars = characters
        self.combination = list(range(combinationLength))   # the previous combination of indices of characters
        self.combination[-1] -= 1                           # set to combination before the first
        n = len(characters)
        self.final = list(range(n - combinationLength, n))  # the final combination of indices of characters

    def next(self):
        """
        :rtype: str
        """
        i = len(self.combination) - 1
        while self.combination[i] == self.final[i]:         # first index that can be incremented
            i -= 1

        self.combination[i] += 1
        for j in range(i + 1, len(self.combination)):
            self.combination[j] = self.combination[j - 1] + 1   # set all next indices in ascending order

        return "".join(self.chars[i] for i in self.combination)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.combination != self.final
