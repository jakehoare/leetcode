_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-hashset/
# Design a HashSet without using any built-in hash table libraries.
# To be specific, your design should include these functions:
# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

# Use list of size 10000 since there are at most 10000 operations so we will not fill every element. There may be
# collisions, which are handled by separate chaining. Use a simple modulo hash function.
# Time - O(1) average case
# Space - O(n)

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hashset = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size          # could use builtin hash() for other objects

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):      # do not add if key already present
            self.hashset[self.hash_function(key)].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):          # do not remove if key not present
            self.hashset[self.hash_function(key)].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashset[self.hash_function(key)] # check inner list