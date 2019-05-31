_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability
# of being returned.

# Maintain a list of the vals as they are added and a mapping from each val to its index in the list.
# Upon removal replace with last val in list (self if removing last val), update mapping for replacement val then
# delete mapping for removed val.
# Note that using a set and no list is also O(1) but pop() does not produce a random val and random.sample is slow.
# Time - O(1)
# Space - O(n)

import random


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = {}   # key is item, value is index in items list
        self.items = []     # list of items

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.mapping:  # append to list and update mapping
            self.items.append(val)
            self.mapping[val] = len(self.items) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.mapping:
            return False
        index = self.mapping[val]
        self.items[index] = self.items[-1]  # replace removed item with last item
        self.mapping[self.items[index]] = index  # update mapping for replacemnt item
        self.items.pop()
        del self.mapping[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # assumes self.items is not empty
        return self.items[random.randint(0, len(self.items) - 1)]